import weakref

from . import _lib
from . import _ffi
from . import _util

from .error import Error
from .util import _is_string

__all__ = ['Connection', 'connect', 'open']

_lib.PQsetErrorVerbosity(1)

def _connect(conninfo):
    return _lib.PQconnectdb(conninfo)

def _connect_start(conninfo):
    return _lib.PQconnectStart(conninfo)

def _connect_poll(conn):
    return _lib.PQconnectPoll(conn)

def _reset(conn):
    return _lib.PQreset(conn)

def _reset_start(conn):
    return _lib.PQresetStart(conn)

def _reset_poll(conn):
    return _lib.PQresetPoll(conn)

def _cancel(conn):
    return _lib.PQcancel(conn)

def _get_result(conn):
    return _lib.PQgetResult(conn)

def _request_c
