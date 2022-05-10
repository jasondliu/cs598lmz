import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(0)
except AttributeError:
    raise ImportError("if_indextoname() not found")

from . import _common

from . import _socket

_socket.socket = socket.socket
_socket.socketpair = socket.socketpair
_socket.fromfd = socket.fromfd
_socket.AF_INET = socket.AF_INET
_socket.AF_UNIX = socket.AF_UNIX
_socket.AF_INET6 = getattr(socket, "AF_INET6", None)
_socket.SOCK_STREAM = socket.SOCK_STREAM
_socket.SOCK_DGRAM = socket.SOCK_DGRAM
_socket.SOCK_RAW = socket.SOCK_RAW
_socket.SOCK_RDM = socket.SOCK_RDM
_socket.SOCK_SEQPACKET = socket.SOCK_SEQPACKET
_socket.SOL_SOCKET = socket.SOL_SOCKET
_socket.SO_RE
