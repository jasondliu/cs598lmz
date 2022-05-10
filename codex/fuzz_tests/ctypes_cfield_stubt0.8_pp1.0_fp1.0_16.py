import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.POINTER = ctypes.POINTER
ctypes.PYFUNCTYPE = ctypes.CFUNCTYPE
ctypes.argtypes = []

def Fun(x, y): pass

ctypes.addressof(Fun)
ctypes.X = type(Fun)
ctypes.bind = ctypes.CFUNCTYPE(None)
ctypes.byref = ctypes.pointer
ctypes.cast = ctypes.cast
ctypes.cdll = ctypes.CDLL
ctypes.create_string_buffer = ctypes.create_string_buffer
ctypes.get_errno = ctypes.get_errno
ctypes.get_last_error = ctypes.get_last_error
ctypes.memmove = ctypes.memmove
ctypes.memset = ctypes.memset
ctypes.pointer = ctypes.pointer
ctypes.reload = ctypes.reload
ctypes.resize = ctypes.resize
ctypes.set_errno = ctypes.set_errno
ctypes.set_last_error
