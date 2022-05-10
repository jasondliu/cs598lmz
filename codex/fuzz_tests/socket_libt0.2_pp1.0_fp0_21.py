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

_g_client_socket = None
_g_client_socket_lock = threading.Lock()
_g_client_socket_thread = None
_g_client_socket_thread_lock = threading.Lock()
_g_client_socket_thread_event = threading.Event()
_g_client_socket_thread_event.set()
_g_client_socket_thread_exit_event = threading.Event()
_g_client_socket_thread_exit_event.set()
_g_client_socket_thread_exit_event_lock = threading.Lock()
_g_client_socket_thread_exit_event_lock.acquire()
_g_client_socket_thread_exit_event_lock.release()
_g_client_socket_thread_exit_event_lock.acquire
