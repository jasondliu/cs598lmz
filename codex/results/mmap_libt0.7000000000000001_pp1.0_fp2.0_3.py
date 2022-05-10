import mmap
import os
import sys
from . import is_windows

from .compat import text_type, binary_type, PY3
from .compat import cBytesIO, cStringIO, cStringIO_init
from . import compat
from . import iostream
from . import ioloop
from . import netutil
from . import process
from . import stack_context
from . import _websocket
from . import _httpclient as httpclient
from .util import b, bytes_type, connection_is_closing, errno_from_exception
from .util import is_valid_ip, timedelta_to_seconds

try:
    import ssl
except ImportError:
    ssl = None


__all__ = [
    "IOStream", "BaseIOStream", "SSLIOStream", "PipeIOStream",
    "TCPServer", "TCPClient", "UnixStreamServer", "UnixStreamClient",
    "UnixDatagramServer", "Resolver",
]

if hasattr(socket, "AF_UNIX"):
    __all__.extend
