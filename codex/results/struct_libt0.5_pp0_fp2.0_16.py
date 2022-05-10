import _struct
import _string
import _sys
import _time
import _thread

from _socket import *

from _socket import __doc__

# This should match the declaration in Modules/socketmodule.h.
if hasattr(_socket, 'socketpair'):
    socketpair = _socket.socketpair

if hasattr(_socket, 'fromfd'):
    fromfd = _socket.fromfd

if hasattr(_socket, 'ntohs'):
    ntohs = _socket.ntohs
    ntohl = _socket.ntohl
    htons = _socket.htons
    htonl = _socket.htonl

if hasattr(_socket, 'inet_aton'):
    inet_aton = _socket.inet_aton
    inet_ntoa = _socket.inet_ntoa

if hasattr(_socket, 'inet_pton'):
    inet_pton = _socket.inet_pton
    inet_ntop = _socket.inet_ntop

if hasattr(_socket, 'getnameinfo'):
    get
