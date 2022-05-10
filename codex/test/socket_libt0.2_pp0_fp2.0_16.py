import socket
import sys
import time

from . import config
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_config = config.load_config()
_g_config.update({'version': version.version_string()})

_g_last_heartbeat_time = 0
_g_last_heartbeat_time_lock = threading.Lock()


def _get_last_heartbeat_time():
    with _g_last_heartbeat_time_lock:
        return _g_last_heartbeat_time


def _set_last_heartbeat_time(time_stamp):
    with _g_last_heartbeat_time_lock:
        global _g_last_heartbeat_time
        _g_last_heartbeat_time = time_stamp


def _get_heartbeat_interval():
    return _g_config['heartbeat_interval']


