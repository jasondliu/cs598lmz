import select
import socket
import sys
import threading
import time

from . import _curl
from . import _curl_easy
from . import _curl_multi
from . import _curl_share
from . import _curl_slist
from . import _curl_version
from . import _util
from . import _util_py2
from . import _util_py3
from . import _util_ssl
from . import _util_thread


__all__ = [
    'Curl',
    'CurlMulti',
    'CurlShare',
]


_logger = logging.getLogger(__name__)


class Curl(object):
    """
    A libcurl easy handle.
    """

    def __init__(self):
        self._handle = _curl_easy.new()
        self._callbacks = {}
        self._response_buffer = BytesIO()
        self._response_headers = {}
        self._response_headers_lock = threading.Lock()
        self._response_headers_list = None
