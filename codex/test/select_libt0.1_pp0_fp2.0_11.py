import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import events
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_is_running = False
_g_is_stopping = False
_g_is_stopped = False
_g_is_restarting = False
_g_is_restarted = False
_g_is_restart_failed = False
_g_is_restart_failed_reason = None
_g_is_restart_failed_detail = None
_g_is_restart_failed_detail_exception = None
_g_is_restart_failed_detail_traceback = None
