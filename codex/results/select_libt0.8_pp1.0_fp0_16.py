import select
import socket
import sys
import threading
import time

from . import log
from .leakdetector import LeakDetector
from .util import thread_exit

_lock = threading.Lock()
_fd2fdni = {}
_fdni2fd = {}
_counter = 0


def _alloc():
    global _counter
    with _lock:
        _counter += 1
        return _counter


def check_closed(fd):
    if isinstance(fd, int):
        fd = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
    if fd.fileno() not in _fdni2fd:
        raise ValueError("I/O operation on closed file")


def fd2fdni(fd):
    if isinstance(fd, int):
        fd = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
    fdni = _fd2fdni.get(fd.fileno(), None)
    if not fdni:
        f
