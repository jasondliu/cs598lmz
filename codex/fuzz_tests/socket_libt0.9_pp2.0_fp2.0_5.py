import socket
import select

try:
    import httplib
except ImportError:
    import http.client as httplib

from .aws4signer import sign, get_v4_credentials
from .imds import InstanceMetadataFetcher, IMDS_TOKEN_BODY, IMDS_TOKEN_HEADER

class _IMDSHTTPConnection(httplib.HTTPConnection):
    '''This class is used to pass requests to the instance metadata server.

    It is knowlegeable of the IMDSv2 token retrieval process and will fill in
    the respective headers of the first request, if necessary.

    It uses a custom `connect` method to ensure connections to the IMDS do not
    trigger interceptor lookups, as the IMDS is only accessible via localhost.
    '''
    def __init__(self, *args, **kwargs):
        self._token = kwargs.pop('token', None)
        self._completed_token_retrieval = False
        httplib.HTTPConnection.__init__(self, *args, **kwargs)


