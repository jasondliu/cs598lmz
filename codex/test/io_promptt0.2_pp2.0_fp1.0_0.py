import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"
    def write(self, b):
        pass

r = MyRawIO()
r.read()
r.read(1)
r.read(2)
r.read(3)
r.read(4)
r.read(5)
r.read(6)
r.read(7)
r.read(8)
r.read(9)
r.read(10)
r.read(11)
r.read(12)
r.read(13)
r.read(14)
r.read(15)
r.read(16)
r.read(17)
r.read(18)
r.read(19)
r.read(20)
r.read(21)
r.read(22)
r.read(23)
r.read(24)
r.read(25)
r.read(26)
r.read(27)
r.read(28)
r
