import weakref
from gevent import socket

from lib.libjsonrpc2.base import JSONRPCError
from lib.libjsonrpc2.jsonrpc import JsonRPC2, HTTP_RESPONSE, HANDLER_INTERFACE

from lib.common import DEBUG
logger = logging.getLogger(__name__)

class HttpJsonRPC2(object):

    '''JsonRPC2 server over http.
    '''

    def __init__(self, self_dispatch=None, handlers=None, logobj=None, profobj=None):
        # default self_dispatch
        self_dispatch = self_dispatch if self_dispatch is not None else HttpJsonRPC2._self_dispatch
        self_dispatch_interface = self._self_dispatch_interface
        if DEBUG:
            self_dispatch_interface = HttpJsonRPC2._self_dispatch_interface
