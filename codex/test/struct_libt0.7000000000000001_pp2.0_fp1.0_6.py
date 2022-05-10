import _struct
import _socket
import _net
import _pypy_socket

# keep a reference to the original socket function before it gets replaced
# by the _pypy_socket one
from socket import socket

try:
    import _socket
except ImportError:
    pass
else:
    socket = _socket.socket
    socketpair = _socket.socketpair
    from _socket import *

# see _pypy_socket.py
AF_NFC = AF_BLUETOOTH = AF_IEEE802154

_blocking_errnos = {
    EAGAIN: _socket.EWOULDBLOCK,
    EALREADY: _socket.EALREADY,
    EINPROGRESS: _socket.EINPROGRESS,
    EWOULDBLOCK: _socket.EWOULDBLOCK,
    WSAEWOULDBLOCK: _socket.EWOULDBLOCK,
    WSAEINPROGRESS: _socket.EINPROGRESS,
}


# ---------------------------- socket object -------------------------------

