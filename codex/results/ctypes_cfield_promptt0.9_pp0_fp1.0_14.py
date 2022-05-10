import ctypes
# Test ctypes.CField
import ctypes.tests.test_cfield as test_cfield

from ctypes import *
from ctypes.util import adr_int

ctypes.c_short.from_address(adr_int(ctypes.__version__)).value
#2078

ctypes.c_char.from_address(adr_int(ctypes.__author__)).value
#117


## Used to show Unicode problems:
#c_wchar_p.from_address(adr_int(ctypes.__doc__)).value

# This should raise MemoryError:
ctypes.c_char.from_address(-42)
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     ctypes.c_char.from_address(-42)
# TypeError: integer < -2**31 to work as a pointer
class POINTER(object):
    """Used to specify a pointer type to type()
    """
    def __init__(self, tp):
        self._type_ = tp

    def _
