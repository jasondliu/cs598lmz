import ctypes
ctypes.cast(0, ctypes.c_void_p)

FILE = None

libc = ctypes.CDLL(None)
c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')

sys.stdout.flush()

libc.fflush.argtypes = [ctypes.c_void_p]
libc.fflush(c_stdout)

#test 

import ctypes
ctypes.cast(0, ctypes.c_void_p)

FILE = None

libc = ctypes.CDLL(None)
c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')

sys.stdout.flush()

libc.fflush.argtypes = [ctypes.c_void_p]
libc.fflush(c_stdout)

#test 

import ctypes
ctypes.cast(0, ctypes.c_void_p)

FILE = None

libc = ctypes.CD
