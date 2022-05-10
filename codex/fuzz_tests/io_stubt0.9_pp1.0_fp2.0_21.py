import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # obtain ownership of buffer
del buf
# The buffer is deallocated now.
# The next line will segfault or fail in some other way.
view[0] = 1
import sys
realloc = ctypes.pythonapi.PyMem_Realloc
realloc.argtypes = (ctypes.c_void_p, ctypes.c_size_t)
realloc.restype = ctypes.c_void_p

def move_around(bufsize):
    buf = ctypes.create_string_buffer(bufsize)
    prev = buf.raw
    while True:
        buf = ctypes.create_string_buffer(bufsize * 4).raw
        bufsize *= 4
        if prev in (ptr() for ptr in gc.get_objects() if isinstance(ptr, ctypes._Pointer)):
            raise AssertionError("memory block was not released")
        prev = buf
        for i in xrange(4):
            buf = realloc(buf, bufsize)
            if bufsize > sys.maxint / 4:
                assert buf is
