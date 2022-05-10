import io
# Test io.RawIOBase()
try:
    io.RawIOBase.readable
except:
    print("SKIP")
    raise SystemExit

class MyRawIOBase(io.RawIOBase):
    def __init__(self):
        self.buf = b''

    def read(self, n=-1):
        return self.buf[:n]

    def write(self, b):
        self.buf += b
        return len(b)

    def close(self):
        pass

# Test io.RawIOBase.read()
buf = MyRawIOBase()
buf.write(b'foo')
print(buf.readable(), buf.writable(), buf.seekable())
print(buf.read(1))
print(buf.read(2))
print(buf.read())

# Test io.RawIOBase.write()
buf = MyRawIOBase()
buf.write(b'foo')
print(buf.buf)
buf.write(b'bar')
print(buf.buf)
buf.write(b'baz')
print(buf.buf)


