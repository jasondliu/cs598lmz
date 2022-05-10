import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import exceptions
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_listen_sock = None
_g_listen_thread = None
_g_listen_thread_stop_event = None
_g_listen_thread_stop_event_lock = threading.Lock()
_g_listen_thread_stop_event_lock_cond = threading.Condition(_g_listen_thread_stop_event_lock)
_g_listen_thread_stop_event_lock_cond_wait_time = 0.1
_g_listen_thread_stop_event_lock_cond_wait_time_max = 5
_g_listen_thread_stop_event_lock_cond_wait_time_step = 0.1
_g_listen_thread_stop_event_lock_cond_
