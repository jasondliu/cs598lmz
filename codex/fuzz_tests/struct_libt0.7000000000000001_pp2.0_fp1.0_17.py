import _struct

from array import array
from fcntl import ioctl
from ctypes import c_int
from ctypes import c_char_p
from ctypes import c_void_p
from ctypes import c_uint
from ctypes import c_uint32
from ctypes import c_uint64
from ctypes import c_byte
from ctypes import c_short
from ctypes import c_ushort
from ctypes import c_char
from ctypes import c_ulong
from ctypes import c_ulonglong
from ctypes import c_float
from ctypes import c_double
from ctypes import Structure
from ctypes import POINTER
from ctypes import CFUNCTYPE
from ctypes import pointer
from ctypes import byref

from kivy.logger import Logger
from kivy.lib import oscAPI
from kivy.lib import oscAPI

from lib.bluetooth import *
from lib.bluetooth import _bt_socket_get_error
from lib.bluetooth import _bt_socket_set_error
from lib.blu
