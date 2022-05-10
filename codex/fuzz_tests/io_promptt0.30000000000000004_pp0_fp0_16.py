import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0

    def readinto(self, b):
        b[:3] = b"foo"
        self.pos += 3
        return 3

    def write(self, b):
        self.pos += len(b)
        return len(b)

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = 50 + pos
        else:
            raise ValueError("Invalid value for 'whence'")
        return self.pos

    def tell(self):
        return self.pos

def test_rawiobase():
    r = MyRawIO()
    assert r.read(10) == b"foo"
    assert r.write(b"bar") == 3
    assert r.seek(5) == 5
    assert r.seek(5, 1) == 10
   
