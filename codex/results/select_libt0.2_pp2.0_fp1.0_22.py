import select
import socket
import sys
import threading
import time
import traceback

from . import _common
from . import _constants
from . import _util
from . import _windows_credentials
from . import _winhttp
from . import _winhttp_errors
from . import _winhttp_helpers
from . import _winhttp_types
from . import _winhttp_utils

_logger = logging.getLogger(__name__)


class _WinHttpRequest(object):
    """A Windows HTTP request.

    This class is not thread-safe.
    """

    def __init__(self, session, url, method, headers, body, proxy_info,
                 redirect_limit, timeout, credentials, flags,
                 auto_detect_proxy_settings):
        self._session = session
        self._url = url
        self._method = method
        self._headers = headers
        self._body = body
        self._proxy_info = proxy_info
        self._redirect_limit = redirect_limit
        self._timeout = timeout
        self._cred
