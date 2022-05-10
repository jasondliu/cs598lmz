import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_server_socket = None
_g_server_thread = None
_g_client_sockets = []
_g_client_threads = []
_g_client_thread_lock = threading.Lock()
_g_client_thread_event = threading.Event()
_g_client_thread_event.set()
