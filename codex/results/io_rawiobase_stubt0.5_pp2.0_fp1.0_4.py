import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def fileno(self):
        return self.fd
    def close(self):
        pass
def open(fd):
    return File(fd)
# }}}

# {{{ ctypes
if sys.version_info[0] == 3:
    import ctypes
    class ctypes_buffer(ctypes.Structure):
        _fields_ = (('buf', ctypes.py_object),
                    ('len', ctypes.c_ssize_t))
    def ctypes_buffer_from_bytes(b):
        return ctypes_buffer(b, len(b))
else:
    import ctypes
    class ctypes_buffer(ctypes.Structure):
        _fields_ = (('buf', ctypes.py_object),
                    ('len', ctypes.c_ssize_t),
                    ('itemsize', ctypes.c_ssize_t),
                    ('readonly', ctypes.c_int),
                    ('ndim', ctypes.c_int),
