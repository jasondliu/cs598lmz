import ctypes
ctypes.cast(ctypes.c_char_p(""), ctypes.c_void_p).value

# How to call a C function from a DLL using ctypes

# ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.
# 
# ctypes is included in Python 2.5 and higher.
# 
# Example
# 
# Load the DLL, and retrieve the function prototype.

>>> import ctypes
>>> lib = ctypes.cdll.LoadLibrary('./libfoo.so')
>>> lib.foo.argtypes = [ctypes.c_int, ctypes.c_int]
>>> lib.foo.restype = ctypes.c_int
>>> lib.foo(1, 2)
3
# 
# The above code works for Linux, for Windows you need to change the extension and prefix of the library.
# 
# See also
# 
# Python/C API
# ctypes documentation
# ctypes tutorial
# Ctypes HOWTO (
