import select
import socket
import sys
import threading
import time

from . import _common
from . import _constants
from . import _errors
from . import _util
from . import _util_posix
from . import _util_windows
from . import _winapi


__all__ = [
    'Pipe', 'PipeConnection', 'PipeListener',
    'pipe', 'pipe_connection', 'pipe_listener',
]


_DEFAULT_BUFFER_SIZE = _constants.DEFAULT_BUFFER_SIZE
_DEFAULT_CHUNK_SIZE = _constants.DEFAULT_CHUNK_SIZE
_DEFAULT_LIMIT = _constants.DEFAULT_LIMIT
_DEFAULT_TIMEOUT = _constants.DEFAULT_TIMEOUT
_DEFAULT_UNIX_SOCKET_TIMEOUT = _constants.DEFAULT_UNIX_SOCKET_TIMEOUT
_DEFAULT_WINDOW_SIZE = _constants.DEFAULT_WINDOW_SIZE
_DEFAULT_WRITE_BUFFER_SIZE = _constants.DE
