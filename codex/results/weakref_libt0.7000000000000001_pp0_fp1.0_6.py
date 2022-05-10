import weakref
from time import time

from twisted.internet.defer import Deferred
from twisted.internet.error import (
    ConnectError,
    ConnectionClosed,
    ConnectionDone,
    ConnectionLost,
    ConnectionRefusedError,
    TCPTimedOutError,
    TimeoutError,
)
from twisted.internet.protocol import Protocol, connectionDone
from twisted.internet.tcp import Client
from twisted.python.failure import Failure
from twisted.web.client import ResponseDone
from twisted.web.http_headers import Headers

from txsocksx.errors import (
    GeneralProxyError,
    ProxyConnectionClosedError,
    ProxyConnectionError,
    ProxyConnectionFailedError,
    ProxyError,
    SOCKS5Error,
)
from txsocksx.tls import TLSMemoryBIOFactory
from txsocksx.websocket.hybi import (
    WebSocketHybiClientFactory,
    WebSocketHybiClientProtocol,
)


class SOCKS5ClientProtocol(Protocol):
    _connectionLostDeferred = None
   
