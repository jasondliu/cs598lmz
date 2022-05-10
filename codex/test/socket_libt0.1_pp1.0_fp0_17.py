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
_g_sock = None
_g_sock_lock = threading.Lock()
_g_sock_thread = None
_g_sock_thread_lock = threading.Lock()
_g_sock_thread_event = threading.Event()
_g_sock_thread_event.set()
_g_sock_thread_event_lock = threading.Lock()
_g_sock_thread_event_lock.acquire()
_g_sock_thread_event_lock.acquire()
_g_sock_thread_event_lock.acquire()
_g_sock_thread_event_lock.acquire()
_g_sock_thread_event_lock.acquire()
_g_sock_
