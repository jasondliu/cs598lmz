import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):

    def read(self, n=-1):
        return b'abc'

    def write(self, b):
        pass

io.RawIOBase.readable = lambda *args: True
io.RawIOBase.writable = lambda *args: True
io.RawIOBase.seekable = lambda *args: True

rawio = MyRawIO()

# test read()
print(rawio.read())
print(rawio.read(0))
print(rawio.read(1))
print(rawio.read(2))
print(rawio.read(3))
print(rawio.read(4))
print(rawio.read(5))
print(rawio.read(6))

# test readall()
