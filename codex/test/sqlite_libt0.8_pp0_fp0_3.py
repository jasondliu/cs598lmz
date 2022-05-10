import ctypes
import ctypes.util
import threading
import sqlite3
import re
from abc import abstractmethod
from functools import partial

from . import networking
from . import util
from . import __version__
from . import exceptions


_logger = logging.getLogger(__name__)

#try:
#    import dns.resolver
#except ImportError:
#    _logger.debug("Error importing DNS resolver")
#    _logger.debug("You won't be able to use DNS features")
#    dns = None

_libc_name = ctypes.util.find_library("c")
if _libc_name is None:
    raise Exception("libc not found")

_libc = ctypes.CDLL(_libc_name, use_errno=True)

if not hasattr(_libc, "setrlimit"):
    raise Exception("libc does not have setrlimit")

if not hasattr(_libc, "getrlimit"):
    raise Exception("libc does not have getrlimit")

