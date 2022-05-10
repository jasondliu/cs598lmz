import ctypes
import ctypes.util
import threading
import sqlite3

from pulsar.managers.manager import Manager
from pulsar.managers.client import Client
from pulsar.utils.sugar import *
from pulsar.utils.system import platform_info, platform_bits
from pulsar.utils.structures import OrderedDict

from . import consts, enums
from .errors import *
from .utils import free_lib


if platform_info()[0] == 'Windows':
    # Windows Hacks!
    _lib = 'msvcrt'
else:
    _lib = 'c'

_libc = ctypes.CDLL(ctypes.util.find_library(_lib), use_errno=True)


_libc.strncpy.argtypes = [
    ctypes.c_char_p, ctypes.c_char_p,
    ctypes.c_ulong]

_libc.strncpy.restype = ctypes.c_char_p

_libc.get_refcount.argtypes = [ctypes.c_void_p]

_libc
