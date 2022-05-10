import ctypes
ctypes.cast(c, ctypes.py_object).value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "stdin").value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "stdout").value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "stderr").value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "__environ").value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "__progname").value

from ctypes import *
c_void_p.in_dll(cdll.LoadLibrary("libc.so.6"), "__signgam").value
