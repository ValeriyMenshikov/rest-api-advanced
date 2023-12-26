from requests import Response
from restclient.client import Restclient
from dm_api_account.models import *


class LoginApi(Restclient):
    def post_v1_account_login(
            self,
            login_credentials_request: LoginCredentials,
            validate_response=True,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param validate_response:
        :param login_credentials_request:
        Authenticate via credentials
        :return:
        """
        response = self.post(
            path=f"/v1/account/login",
            json=login_credentials_request.model_dump(exclude_none=True),
            **kwargs
        )
        if validate_response:
            UserEnvelope(**response.json())
        return response

    def del_v1_account_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        response = self.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )
        return response

    def del_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """
        response = self.delete(
            path=f"/v1/account/login",
            **kwargs
        )
        return response
