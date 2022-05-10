import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=0):
        return b''
    def write(self, buf):
        return 0
m = MyRawIO()
