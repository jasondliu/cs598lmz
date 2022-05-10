import socket
import sys
import time

from . import common
from . import config
from . import constants
from . import exceptions
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_rpc_server = None
_g_rpc_server_thread = None


def _get_rpc_server():
    global _g_rpc_server
    if _g_rpc_server is None:
        _g_rpc_server = RPCServer()
    return _g_rpc_server


def _get_rpc_server_thread():
    global _g_rpc_server_thread
    if _g_rpc_server_thread is None:
        _g_rpc_server_thread = threading.Thread(target=_get_rpc_server().serve_forever)
        _g_rpc_server_thread.setDaemon(True)
        _g_rpc_server_thread.start()
