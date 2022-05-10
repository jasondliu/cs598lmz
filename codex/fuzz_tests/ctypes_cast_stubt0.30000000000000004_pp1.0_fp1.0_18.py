import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

from rpython.rlib.rstring import StringBuilder
from rpython.rlib.rstruct.nativefmttable import native_is_bigendian
from rpython.rlib.rstruct.runpack import runpack
from rpython.rlib.rstruct.rstruct import unpack_from_string
from rpython.rlib.rstruct.rstruct import unpack_from_string_loop
from rpython.rlib.rstruct.rstruct import unpack_from_string_one
from rpython.rlib.rstruct.rstruct import unpack_from_string_one_loop
from rpython.rlib.rstruct.rstruct import pack_into_string
from rpython.rlib.rstruct.rstruct import pack_into_string_loop
from rpython.rlib.rstruct.rstruct import calcsize
from rpython.rlib.rstruct.rstruct import calcsize_loop
from rpython.rlib.rstruct.rstruct import pack
from rpython.rlib
