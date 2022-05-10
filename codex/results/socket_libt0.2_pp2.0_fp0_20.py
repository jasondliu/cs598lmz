import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_rpc_server = None
_g_rpc_server_thread = None
_g_rpc_server_thread_lock = threading.Lock()
_g_rpc_server_thread_cond = threading.Condition()
_g_rpc_server_thread_stop_flag = False


def _rpc_server_thread_proc():
    global _g_rpc_server_thread_stop_flag
    _logger.info('_rpc_server_thread_proc start')
    while True:
        _g_rpc_server_thread_cond.acquire()
        if _g_rpc_server_thread_stop_flag:
            _g_rpc_server_thread_cond.release()
            break
        _g
