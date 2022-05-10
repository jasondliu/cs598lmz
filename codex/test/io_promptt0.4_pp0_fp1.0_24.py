import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'0' * n
    def write(self, b):
        return len(b)

r = MyRawIO()
print(r.read(10))
print(r.write(b'abcdef'))
