import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b'abc'
    def write(self, b):
        return len(b)

r = MyRawIO()
r.read()
r.write(b'def')
r.seekable()
r.readable()
r.writable()
