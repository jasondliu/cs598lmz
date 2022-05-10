import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_char(b'abc')),ctypes.c_void_p)

class Py_buffer(ctypes.Structure):
    _fields_ = [
        ("buf", ctypes.py_object),  # void*
        ("obj", ctypes.py_object),
        # The following are exposed in the Python C API but not documented.
        ("suboffsets", ctypes.py_object),
        ("internal", ctypes.c_char_p),
        # Structure members below this point are rarely exposed.
        ("format", ctypes.c_char_p),
        ("ndim", ctypes.c_int),
        ("shape", ctypes.py_object),
        ("strides", ctypes.py_object),
        ("itemsize", ctypes.c_int),
        # These flags are only present in recent Python versions.
        ("readonly", ctypes.c_int),  # bool
        ("FORMAT_STRING", ctypes.c_char_p),
        ("internal_len", ctypes.c_int
