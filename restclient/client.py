from requests import Session, Response

from session import LoggedSession


class Restclient:
    def __init__(self, host, session: Session = None):
        self.host = host
        self.session = session or Session()

    def post(self, path: str, **kwargs) -> Response:
        return self.session.post(url=self._build_path(path), **kwargs)

    def get(self, path: str, **kwargs) -> Response:
        path = self._build_path(path)
        return self.session.get(url=self._build_path(path), **kwargs)

    def put(self, path: str, **kwargs) -> Response:
        path = self._build_path(path)
        return self.session.put(url=self._build_path(path), **kwargs)

    def delete(self, path: str, **kwargs) -> Response:
        path = self._build_path(path)
        return self.session.delete(url=self._build_path(path), **kwargs)

    def _build_path(self, path):
        return self.host + path
