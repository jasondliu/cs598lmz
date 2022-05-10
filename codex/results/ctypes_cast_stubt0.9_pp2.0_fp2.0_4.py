import ctypes
ctypes.cast(1327, ctypes.py_object)
 

ctypes.pydll.msvcrt.free.restype = None
ctypes.pydll.msvcrt.free.argtypes = [ctypes.c_void_p]

ctypes.pydll.msvcrt.malloc.restype = ctypes.c_void_p
ctypes.pydll.msvcrt.malloc.argtypes = [ctypes.c_size_t]

class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

PyObject._fields_ = [
    ("ob_refcnt", ctypes.c_long),
    ("ob_type", ctypes.POINTER(PyObject)),
    ]

class GcHead(ctypes.Structure):
    _fields_ = [
        ("gc", ctypes.c_ubyte),
        ("_gc_next", ctypes.c_void_p),
        ("_gc_prev", ctypes.c
