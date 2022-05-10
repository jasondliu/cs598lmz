import _struct
import sys
import time
import traceback

from ctypes import *

from psutil._common import *
from psutil._compat import check_unicode_path
from psutil._psposix import net_if_addrs
# --- constants


def enum(**enums):
    """A Pythonic version of C/C++ enum."""
    return type('Enum', (), enums)

AF_UNIX = enum(SOCK_STREAM=1, SOCK_DGRAM=2)
AF_INET = enum(SOCK_STREAM=1, SOCK_DGRAM=2)
AF_INET6 = enum(SOCK_STREAM=1, SOCK_DGRAM=2)

_CONN_STATE = {
    0x01: const("ESTABLISHED"),
    0x02: const("SYN_SENT"),
    0x03: const("SYN_RECV"),
    0x04: const("FIN_WAIT1"),
    0x05: const("FIN_WAIT2"),
    0x
