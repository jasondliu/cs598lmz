import io
# Test io.RawIOBase
import io

class RawI(io.RawIOBase):

    def read(self, n=-1):
        return b'abc'

    def write(self, b):
        return len(b)

r = RawI()
print(r.read())
print(r.read(2))
print(r.read(4))
print(r.read())
print(r.read1(1))
print(r.readinto(bytearray(3)))
print(r.readinto1(bytearray(3)))
print(r.readinto(bytearray(1)))
print(r.readinto1(bytearray(1)))
print(r.write(b'xyz'))
print(r.write(b'xyz'*100))
print(r.seekable())
print(r.readable())
print(r.writable())
print(r.seek(10))
print(r.tell())
print(r.truncate(10))
print(r.fileno())
print(r.isatty())
