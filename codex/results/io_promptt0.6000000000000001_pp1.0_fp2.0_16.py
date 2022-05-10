import io
# Test io.RawIOBase
import io
import _io

if hasattr(_io, 'RawIOBase'):
    class C(_io.RawIOBase):
        def readinto(self, b):
            return 5
        def write(self, b):
            return len(b)
        def readable(self):
            return True
        def writable(self):
            return True
        def seekable(self):
            return True
        def read(self, n=-1):
            return b'x'*n
        def seek(self, n, whence=0):
            return 0
        def tell(self):
            return 0
        def close(self):
            pass
    c = C()
    assert c.readinto(bytearray(10)) == 5
    assert c.readinto(memoryview(bytearray(10))) == 5
    assert c.write(b'x') == 1
    assert c.write(bytearray(b'x')) == 1
    assert c.write(memoryview(b'x')) == 1
    assert c.readable()

