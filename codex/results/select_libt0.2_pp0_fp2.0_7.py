import select
import socket
import struct
import sys
import time
import traceback

from . import _common
from . import _util
from . import _win32
from . import _win32_pipe
from . import _win32_socket
from . import _win32_event
from . import _win32_file
from . import _win32_handle
from . import _win32_process
from . import _win32_security
from . import _win32_service
from . import _win32_thread
from . import _win32_timer
from . import _win32_waitable
from . import _win32_wsa

from ._common import (
    _PY2,
    _PY3,
    _PY34,
    _PY35,
    _PY36,
    _PY37,
    _PY38,
    _PY39,
    _PYPY,
    _PYPY3,
    _WIN32,
    _WIN64,
    _WINDOWS,
    _POSIX,
    _POSIX2,

