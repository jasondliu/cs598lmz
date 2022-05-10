import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b)
        data = self.file.read(n)
        b[:len(data)] = data
        return len(data)

import ctypes
libc = ctypes.CDLL(None)
c_ssize_t = ctypes.c_ssize_t
c_void_p = ctypes.c_void_p

class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

PyObject._fields_ = [
    ("refcnt", ctypes.c_long),
    ("type", ctypes.c_void_p)
]

class PyVarObject(ctypes.Structure):
    _fields_ = [("ob_size", ctypes.c_long)]

class PyBytesObject(PyVarObject):
    _fields_ = [("ob_shash", ctypes.c
