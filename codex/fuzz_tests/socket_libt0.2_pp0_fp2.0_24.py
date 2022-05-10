import socket
import sys
import threading
import time
import traceback

from . import config
from . import constants
from . import exceptions
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_lock = threading.Lock()
_g_client_socket = None
_g_client_socket_lock = threading.Lock()
_g_client_socket_thread = None
_g_client_socket_thread_lock = threading.Lock()
_g_client_socket_thread_stop = False
_g_client_socket_thread_stop_lock = threading.Lock()
_g_client_socket_thread_stop_event = threading.Event()
_g_client_socket_thread_stop_event.set()
_g_client_socket_thread_stop_event_lock = threading.Lock()
_g_client_socket_thread_stop_event_lock.acquire()
_g_client_socket_thread_stop_event_lock.release()
