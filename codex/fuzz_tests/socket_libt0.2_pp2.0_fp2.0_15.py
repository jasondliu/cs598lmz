import socket
import sys
import threading
import time

from . import config
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_is_running = False
_g_is_stopping = False
_g_is_stopped = False
_g_is_restarting = False
_g_is_restarted = False
_g_is_restart_failed = False
_g_is_restart_failed_reason = ''
_g_is_restart_failed_detail = ''
_g_is_restart_failed_exception = None
_g_is_restart_failed_traceback = None
_g_is_restart_failed_time = 0
_g_is_restart_failed_time_str = ''
_g_is_restart_failed_time_str_short = ''
_g_is_restart_failed_time_str_short_2 = ''
_g_is_restart_failed_time_str
