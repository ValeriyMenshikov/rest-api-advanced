from requests import Response
from restclient.client import Restclient
from dm_api_account.models import *
from restclient.session import LoggedSession


class AccountApi(Restclient):

    def post_v1_account(
            self,
            registration_request: Registration,
            **kwargs
    ) -> Response:
        """
        :param registration_request:
        Register new user
        :return:
        """
        response = self.post(
            path=f"/v1/account",
            json=registration_request.model_dump(exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(
            self,
            validate_response=True,
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """
        response = self.get(
            path=f"/v1/account",
            **kwargs
        )
        if validate_response:
            return UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            validate_response=True,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Activate registered user
        :param validate_response:
        :param token: str
        :return:
        """
        response = self.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            reset_password_request: ResetPassword,
            validate_response=True,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Reset registered user password
        :param validate_response:
        :param reset_password_request:
        :return:
        """
        response = self.post(
            path=f"/v1/account/password",
            json=reset_password_request.model_dump(exclude_none=True),
            **kwargs
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            change_password_request: ChangePassword,
            validate_response=True,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user password
        :param change_password_request:
        :param validate_response:
        :return:
        """
        response = self.put(
            path=f"/v1/account/password",
            json=change_password_request.model_dump(exclude_none=True),
            **kwargs
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            change_email_request: ChangeEmail,
            validate_response=True,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user email
        :param validate_response:
        :param change_email_request:
        :return:
        """
        response = self.put(
            path=f"/v1/account/email",
            json=change_email_request.model_dump(exclude_none=True),
            **kwargs
        )
        if validate_response:
            return UserEnvelope(**response.json())
        return response


client = AccountApi(host='http://5.63.153.31:5051', session=LoggedSession()).post_v1_account(registration_request=Registration(login='123', password='123123', email='123123'))
