import select
import socket
import sys
import time

from . import _compat
from . import _util
from . import _util_posix
from . import _util_windows
from . import _winapi


__all__ = [
    'PIPE', 'STDOUT', 'DEVNULL', 'SubprocessError', 'CalledProcessError',
    'TimeoutExpired', 'CompletedProcess', 'Popen', 'run', 'check_call',
    'check_output', 'call', 'getstatusoutput', 'getoutput', 'list2cmdline',
    'check_output', 'DEFAULT_TIMEOUT', 'TimeoutExpired',
]

# Some constants from the POSIX standard which we use
ECHILD = _util_posix.ECHILD
EINTR = _util_posix.EINTR
EINVAL = _util_posix.EINVAL
ENOENT = _util_posix.ENOENT
ECHO = _util_posix.ECHO

# Some constants from the Windows API which we use
