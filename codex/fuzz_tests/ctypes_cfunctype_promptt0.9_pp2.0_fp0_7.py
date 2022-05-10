import ctypes
# Test ctypes.CFUNCTYPE()

def py_dummy_stdcall(v0):
    #print('py_dummy_stdcall:', v0)
    return v0

def py_dummy_cdecl(v0):
    #print('py_dummy_cdecl:', v0)
    return v0


if sys.int_info.size == 8:
    STDPROC_PTR = ctypes.WINFUNCTYPE(ctypes.c_uint, ctypes.c_uint)
    CDECLPROC_PTR = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint)
    STDPROC = STDPROC_PTR(py_dummy_stdcall)
    CDECLPROC = CDECLPROC_PTR(py_dummy_stdcall)
else:
    STDPROC_PTR = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_uint)
    CDECLPROC_PTR = ctypes.CFUNCTYPE(ctypes
