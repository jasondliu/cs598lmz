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


