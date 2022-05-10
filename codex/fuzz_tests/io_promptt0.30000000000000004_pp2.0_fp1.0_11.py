import io
# Test io.RawIOBase()

class MyRawIO(io.RawIOBase):

    def read(self, n=-1):
        return b'\x00'*n

    def write(self, b):
        return len(b)

try:
    io.RawIOBase()
except TypeError:
    print('TypeError')

try:
    io.RawIOBase(None)
except TypeError:
    print('TypeError')

print(MyRawIO().read(10))
print(MyRawIO().write(b'abc'))
