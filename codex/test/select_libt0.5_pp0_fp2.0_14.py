import select
import sys
import time
import traceback

from ws4py.client.threadedclient import WebSocketClient

from .. import __version__
from .. import pb
from .. import util
from .. import ws_util
from ..ws_server import ws_server
from ..ws_util import websocket_connect

_log = logging.getLogger(__name__)

#
# Client
#

class Client(object):
    def __init__(self, url, server_name, server_key, server_cert,
                 client_name=None, client_key=None, client_cert=None,
                 verify_server=True, verify_client=True,
                 timeout=None, websocket_timeout=None):
        self.url = url
        self.server_name = server_name
        self.server_key = server_key
        self.server_cert = server_cert
        self.client_name = client_name
        self.client_key = client_key
        self.client_cert = client_cert
        self.verify
