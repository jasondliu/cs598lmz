import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_local_ip = None
_g_local_ip_lock = threading.Lock()


def get_local_ip():
    global _g_local_ip
    with _g_local_ip_lock:
        if _g_local_ip is None:
            _g_local_ip = _get_local_ip()
        return _g_local_ip


def _get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        _logger.error(r'get_local_ip failed : {}'.format(e),
