import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_lock = threading.Lock()
_g_threads = []
_g_threads_lock = threading.Lock()
_g_threads_cond = threading.Condition()
_g_threads_cond_lock = threading.Lock()
_g_threads_cond_notify_all = False
_g_threads_cond_notify_all_lock = threading.Lock()
_g_threads_cond_notify_all_cond = threading.Condition()
_g_threads_cond_notify_all_cond_lock = threading.Lock()
_g_threads_cond_notify_all_cond_notify_all = False
_g_threads_cond_notify_all_cond_notify_all_lock = threading.Lock()
