import select
import socket
import sys
import threading
import time

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_server_sock = None
_g_server_thread = None
_g_server_thread_stop_event = None
_g_server_thread_stop_event_lock = threading.Lock()
_g_server_thread_stop_event_lock_cond = threading.Condition(_g_server_thread_stop_event_lock)
_g_server_thread_stop_event_lock_cond_notify_all = lambda: _g_server_thread_stop_event_lock_cond.notify_all()
_g_server_thread_stop_event_lock_cond_wait = lambda: _g_server_thread_stop_event_lock_cond.wait()
_g_server_thread_stop_event_lock_cond_
