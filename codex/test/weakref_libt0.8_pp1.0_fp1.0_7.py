import weakref

from . import utils
from .client import Client
from .client import ClientDisconnected
from .client import ClientConnected
from .client import ClientDataReceived
from .client import ClientDataSent

from .. import exceptions
from ..log import logger
from ..message import Message


class Remote(object):

    def __init__(self, parent, ip, port, **kwargs):
        self.parent = weakref.proxy(parent)
        self.ip = ip
        self.port = port

        self.clients = {}
        self.max_clients = kwargs.get('max_clients', 10)
        self.allow_tunnel = kwargs.get('allow_tunnel', True)

        self.ping_timeout = kwargs.get('ping_timeout', 5)

        self.on_connect = kwargs.get('on_connect')
        self.on_disconnect = kwargs.get('on_disconnect')
        self.on_receive = kwargs.get('on_receive')
