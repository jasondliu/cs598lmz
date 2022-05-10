import gc, weakref
import gevent.socket as socket
from zmqinterface.Socket import Socket
from zmqinterface import messaging

logger = logging.getLogger('zmqinterface')
#logger.setLevel(logging.DEBUG)
try:
    import gevent.core
    gevent_core = gevent.core
except ImportError:
    gevent_core = None

try:
    from .socket import Socket
    from .messaging import *
except ValueError:
    from socket import Socket
    from messaging import *


class Interface(object):
    def __init__(self, ctx=None, socket_timeout=None):
        if ctx is None:
            self._ctx = zmq.Context.instance()
            self._own_context = True
        else:
            self._ctx = ctx
            self._own_context = False

        self.socket_timeout = socket_timeout
        self._prog_pairs = {} # socket prog_id => (socket, prog_id)
        self._garbage_collect_tasks_by_ref 
