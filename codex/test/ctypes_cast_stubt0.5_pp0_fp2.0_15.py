import ctypes
ctypes.cast(0, ctypes.py_object)

#from ctypes import *
#cast(0, py_object)

from ctypes import py_object
py_object(0)

py_object(None)

py_object(True)

py_object(False)

from ctypes import c_char, c_int
py_object(c_char(b'x'))

py_object(c_int(42))

from ctypes import c_char_p, c_void_p
py_object(c_char_p(b'hello'))

py_object(c_void_p(0))

from ctypes import c_int, c_double, c_void_p
a = c_int(42)
a.value

b = c_double(3.14)
b.value

