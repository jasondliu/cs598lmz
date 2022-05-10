import select
import socket
import sys
import threading
import time
import traceback
import types
import weakref

from . import _common
from . import _constants
from . import _errors
from . import _events
from . import _ffi
from . import _util
from . import _tls
from . import _tls_legacy
from . import _tls_openssl
from . import _tls_securetransport
from . import _tls_stdio
from . import _tls_windows


__all__ = ['Loop', 'Handle', 'Timer', 'Signal', 'Idle', 'Prepare', 'Check',
           'Async', 'Event', 'Stream', 'TCP', 'Pipe', 'TTY', 'UDP', 'Poll',
           'Process', 'SignalChecker', 'default_loop', 'get_event_loop',
           'set_event_loop', 'new_event_loop', 'set_debug']


_LOOP_CALLBACKS = {
    _ffi.UV_RUN: '_run',
    _ff
