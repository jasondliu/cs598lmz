import codecs
codecs.register_error("strict", codecs.ignore_errors)

from math import *
import sys
PY3 = sys.version > '3'

from ctypes import *
from mod_pywebsocket.common.data_types import *
from mod_pywebsocket.common.utils import *


def _generate_websocket_client_handshake_headers(port, resource):
    return (
        'GET %s HTTP/1.1\r\n'
        'Host: localhost:%d\r\n'
        'Connection: Upgrade\r\n'
        'Sec-WebSocket-Key1: %s\r\n'
        'Sec-WebSocket-Key2: %s\r\n'
        'Upgrade: WebSocket\r\n\r\n'
        '%s\r\n') % (resource, port,
                 _generate_random_key(random.randint(1, 12)),
                 _generate_random_key(random.randint(1, 12)),
                 _generate_key3(8))



