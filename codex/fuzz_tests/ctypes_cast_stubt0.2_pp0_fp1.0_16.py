import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
#
#  PyPy's ctypes
#
# ___________________________________________________________________________

from pypy.rpython.lltypesystem import rffi
from pypy.rpython.tool import rffi_platform as platform
from pypy.rpython.lltypesystem.lltype import Signed, Unsigned, Bool, Char, UniChar
from pypy.rpython.lltypesystem.lltype import Float, SingleFloat, DoubleFloat
from pypy.rpython.lltypesystem.lltype import Void, nullptr
from pypy.rpython.lltypesystem.lltype import Ptr, Struct, Array, GcStruct
from pypy.rpython.lltypesystem.lltype import pyobjectptr
from pypy.rpython.lltypesystem.lltype import malloc, free
from pypy.rpython.lltypesystem.lltype import cast_opaque_ptr
from pypy.rpython.lltypesystem.lltype import cast_primitive
from pypy.rpython
