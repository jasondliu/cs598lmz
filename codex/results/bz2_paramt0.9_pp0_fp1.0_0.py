from bz2 import BZ2Decompressor
BZ2Decompressor()

from lxml import etree
from StringIO import StringIO

from caldav.lib.error import CalDAVHTTPError as HTTPError
from caldav.lib.error import CalDAVHTTPErrorWithResponse as HTTPErrorWithResponse
from caldav.lib.error import CalDAVHTTPErrorNotFound as HTTPErrorNotFound

from caldav.lib.url import URL, urldefrag, joinURL


log = logging.getLogger("caldav.lib.request")

__all__ = [
    "Request",
    "Report",
]

class RequestMixIn(object):
    """Mixin class for HTTP requests we use for CalDAV."""

    def __init__(self, method, url, body=None, headers=None, environ=None):
        if headers is None:
            headers = {}
        self.method = method
        self.url = url
        self.body = body
        self.headers = Headers(headers)
        self.environ = environ

    @property
    def host_port(self):
       
