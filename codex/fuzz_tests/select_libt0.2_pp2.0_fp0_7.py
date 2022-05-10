import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import constants
from . import exceptions
from . import utils
from . import websocket_client
from . import websocket_server
from . import websocket_uri

log = logging.getLogger(__name__)


class WebSocketApp(object):
    """
    Higher level of APIs are provided.
    The interface is like JavaScript WebSocket object.
    """

    def __init__(self, url,
                 header=None,
                 on_open=None,
                 on_message=None,
                 on_error=None,
                 on_close=None,
                 keep_running=True,
                 get_mask_key=None,
                 cookie=None,
                 subprotocols=None,
                 on_cont_message=None,
                 on_data=None,
                 on_ping=None,
                 on_pong=None,
                 on_cont_data=None,
                 on_cont_ping=None,
                 on_
