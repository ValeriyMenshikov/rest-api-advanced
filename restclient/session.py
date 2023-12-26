import uuid

import curlify
import requests
import structlog as structlog
from requests import Session, Response

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class LoggedSession(Session):
    log = structlog.get_logger(__name__).bind(service='api')

    def request(
            self,
            method,
            url,
            params=None,
            data=None,
            headers=None,
            cookies=None,
            files=None,
            auth=None,
            timeout=None,
            allow_redirects=True,
            proxies=None,
            hooks=None,
            stream=None,
            verify=None,
            cert=None,
            json=None
    ) -> Response:

        log = self.log.bind(evet_id=str(uuid.uuid4()))

        log.msg(
            event='request',
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json,
            data=data
        )

        rest_response = super().request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
            files=files,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert,
            json=json,
        )
        curl = curlify.to_curl(rest_response.request)
        print(curl)
        log.msg(
            event='response',
            status_code=rest_response.status_code,
            headers=rest_response.headers,
            json=self._get_json(rest_response),
            text=rest_response.text,
            content=rest_response.content,
        )
        rest_response.raise_for_status()
        return rest_response

    @staticmethod
    def _get_json(rest_response):
        try:
            return rest_response.json()
        except requests.exceptions.JSONDecodeError:
            return


