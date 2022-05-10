import ctypes
ctypes.cast(0, ctypes.c_void_p)

FILE = None

libc = ctypes.CDLL(None)
c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')

