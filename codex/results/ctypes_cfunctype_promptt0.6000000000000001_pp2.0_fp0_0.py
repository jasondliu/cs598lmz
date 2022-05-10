import ctypes
# Test ctypes.CFUNCTYPE()
def func(x,y):
    return x+y

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
f(2,3)

# Test ctypes.pythonapi
ctypes.pythonapi.Py_GetVersion()

# Test ctypes.pydll
ctypes.pydll.Py_GetVersion()

# Test ctypes.cdll
ctypes.cdll.msvcrt.rand()

# Test ctypes.util
ctypes.util.find_library('c')

# Test ctypes.string_at
ctypes.string_at(ctypes.c_int(0), 4)

# Test ctypes.wstring_at
ctypes.wstring_at(ctypes.c_int(0), 4)

# Test ctypes.get_errno
ctypes.get_errno()

# Test ctypes.set_errno
ctypes.set_errno(0)

# Test ctypes.get
