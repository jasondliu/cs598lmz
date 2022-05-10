import select
# Test select.select() to see if it supports timeout
try:
    select.select([], [], [], 0.1)
except select.error:
    # select.error: (4, 'Interrupted system call')
    raise ImportError("select.select() doesn't support timeout")

from . import _socket
from . import _ssl
from . import _fileobject
from ._fileobject import *

__all__ = _socket.__all__ + _ssl.__all__ + _fileobject.__all__

if hasattr(_socket, "ssl"):
    __all__.append("ssl")
    ssl = _socket.ssl

if hasattr(_socket, "wait_read"):
    __all__.append("wait_read")
    wait_read = _socket.wait_read

if hasattr(_socket, "wait_write"):
    __all__.append("wait_write")
    wait_write = _socket.wait_write

if hasattr(_socket, "wait_readwrite"):
    __all__.append("wait_readwrite")
    wait_
