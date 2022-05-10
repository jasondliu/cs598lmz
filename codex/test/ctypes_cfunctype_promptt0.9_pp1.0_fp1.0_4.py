import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *
from ctypes import util
PYLIB = util.find_library("python")
LIBC = CDLL(PYLIB)
from _ctypes import FUNCFLAG_CDECL
from ctypes import _CFuncPtr
from ctypes import cast, POINTER
#


from ctypes import *
import platform
