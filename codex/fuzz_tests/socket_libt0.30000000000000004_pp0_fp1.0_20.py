import socket
import sys
import threading
import time
import traceback

from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_thread_pool = []
_g_thread_pool_lock = threading.Lock()
_g_thread_pool_stop = False


def _thread_pool_monitor():
    while True:
        time.sleep(10)
        with _g_thread_pool_lock:
            if _g_thread_pool_stop:
                break
            for t in _g_thread_pool:
                if not t.is_alive():
                    _logger.warning('thread {} is not alive'.format(t.name))
                    _g_thread_pool.remove(t)
                    t.join()
    _logger.info('thread_pool_monitor exit')


def _thread_pool_start():
    _g_thread_pool_stop = False
    t = threading.Thread(target=_thread_pool_monitor, name
