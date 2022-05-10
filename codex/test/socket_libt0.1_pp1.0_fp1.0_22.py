import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import exceptions
from . import log
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_thread_pool = None
_g_thread_pool_lock = threading.Lock()
_g_thread_pool_cond = threading.Condition(_g_thread_pool_lock)
_g_thread_pool_thread_count = 0
_g_thread_pool_thread_count_lock = threading.Lock()
_g_thread_pool_thread_count_cond = threading.Condition(_g_thread_pool_thread_count_lock)
_g_thread_pool_thread_count_max = 0
_g_thread_pool_thread_count_min = 0
_g_thread_pool_thread_count_min_lock = threading.Lock()
