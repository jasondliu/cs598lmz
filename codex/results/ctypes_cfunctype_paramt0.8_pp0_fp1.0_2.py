import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
print(FUNTYPE)
print(FUNTYPE(1))
ctypes.pythonapi.PyRun_SimpleString(b'print("Hello, world!")\n')

# pointers
print(ctypes.POINTER(ctypes.c_int))

# function pointers
import ctypes
FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
print(FUNC_TYPE)
print(FUNC_TYPE(1))


# -*- coding: iso-8859-1 -*-
import ctypes
# find library
import ctypes.util
print(ctypes.util.find_library('c'))
print(ctypes.util.find_library('m'))

libc = ctypes.CDLL(ctypes.util.find_library('c'))
print(libc)
print(hasattr(libc, 'printf'))

# call library function
# libc.printf(b'Hello %s\n', b'World')


# -
