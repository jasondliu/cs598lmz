import _struct
import _librequest
from srv.srv_client import Request as BaseRequest
from srv.srv_client import RequestException


class Request(BaseRequest):
    def __init__(self, srv_client, method, url, content=None, headers=None):
        """
        @param content: if None, indicates a "GET" request;
                        if "" (empty string), indicates a "POST" without a body;
                        otherwise, a "POST" with a body
        """
        BaseRequest.__init__(self, srv_client, method, url, content, headers)
        self.__c_reque
