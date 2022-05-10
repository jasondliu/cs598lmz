import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

p = ctypes.cast(view, ctypes.POINTER(ctypes.c_byte))

read = ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)(lambda p, size: ctypes.c_size_t(0))
write = ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t)(lambda p, size: ctypes.c_size_t(0))
seek = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int64, ctypes.c_int)(lambda p, offset, whence: ctypes.c_int(0))
close = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(lambda p: ctypes.c_int(0))

def callback(self, method):
    return ctypes.cast
