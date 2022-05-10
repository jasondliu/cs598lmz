import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n

def test_File_read():
    f = File()
    assert f.read(0) == b''
    assert f.read(5) == b'\x00' * 5
    assert f.read() == b'\x00' * (sys.maxsize - 5)
    assert f.read() == b''

class File2(io.RawIOBase):
    def readinto(self, b):
        return b.__reduce__()[2]['size']

def test_File2_readinto():
    f = File2()
    b = bytearray(10)
    assert f.readinto(b) == 10
    assert b == b'\x00' * 10

class File3(io.RawIOBase):
    def readinto(self, b):
        return b.__reduce__()[2]['size']

def test_File3_readinto():
    f = File3()
    b = bytearray
