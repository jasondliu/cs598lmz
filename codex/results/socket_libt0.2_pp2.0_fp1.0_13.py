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
from . import xlog

xlog.log_init()

logger = xlog.getLogger("x_tunnel")
logger.set_buffer(500)

# global config
g_config = config.load()

# global var
g_running = False
g_handler = None
g_server_thread = None
g_client_thread = None
g_server_sock = None
g_client_sock = None
g_server_conn = None
g_client_conn = None
g_server_conn_lock = threading.Lock()
g_client_conn_lock = threading.Lock()
g_server_conn_cond = threading.Condition(g_server_conn_lock)
g_client_conn_cond = threading.Condition(g_client_conn_lock)
g_server_conn_id = 0
g_client_conn_id =
