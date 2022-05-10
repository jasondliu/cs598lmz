import io
# Test io.RawIOBase, io.RawIOBase.readall
class C(io.RawIOBase):
    def readable(self): return True
    def readinto(self, b):
        b[:1] = b'\x00'
        return 1
    def readall(self):
        return b'abc'
    def write(self, b):
        raise NotImplementedError

class D(C):
    def readable(self):
        raise Exception

def test(c):
    b = bytearray()
    for i in range(4):
        b += bytes(c.read(1))
    assert b == b'\000abc'
    assert c.readall() == b''
    raises(Exception, "c.readall()")

