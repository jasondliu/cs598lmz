import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_stop_event = threading.Event()
_g_stop_event.set()

_g_thread = None
_g_thread_lock = threading.Lock()


def start_service(port):
    global _g_thread
    with _g_thread_lock:
        if _g_thread is None:
            _g_thread = threading.Thread(target=_service_thread, args=(port,))
            _g_thread.start()
            _g_stop_event.clear()


def stop_service():
    global _g_thread
    with _g_thread_lock:
        if _g_thread is not None:
            _g_stop_event.set()
            _g_thread.join()
            _g_thread = None


