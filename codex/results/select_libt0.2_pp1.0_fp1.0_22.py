import select
import socket
import sys
import time
import traceback

from . import __version__
from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_server_socket = None
_g_server_thread = None
_g_server_thread_stop_event = None
_g_server_thread_stop_event_lock = threading.Lock()
_g_server_thread_stop_event_lock_cond = threading.Condition(_g_server_thread_stop_event_lock)
_g_server_thread_stop_event_lock_cond_notify = True
_g_server_thread_stop_event_lock_cond_notify_lock = threading.Lock()
_g_server_thread_stop_event_lock_cond_notify_lock_cond = threading.Condition(_g_server_thread_stop_event_lock_cond_notify_lock)
_g_server_
