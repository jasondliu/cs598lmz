import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStructOrUnion = type(S)

# Uncomment before this test is included in the test suite:
#ctypes.Array = type([1])

ctypes.PyCSimpleType = type(ctypes.c_int)

ctypes.Py_ssize_t = ctypes.c_int

ctypes.CArgObject = type(ctypes.byref(ctypes.c_int()))


# ctypes.wintypes types not defined on Windows
class FILETIME(ctypes.Structure): pass
ctypes.FILETIME = FILETIME

class OVERLAPPED(ctypes.Structure): pass
ctypes.OVERLAPPED = OVERLAPPED

ctypes.wintypes.HANDLE = ctypes.c_int
ctypes.wintypes.BOOL = ctypes.c_int
ctypes.wintypes.HMODULE = ctypes.c_int

ctypes.wintypes.DWORD = ctypes.c_uint
ctypes.wintypes.LPARAM = ctypes.c
