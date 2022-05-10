import io
# Test io.RawIOBase for readinto()
class FileIO(io.RawIOBase):

    def readinto(self, b):
        b[:] = b"\x00\x01\x02\x03"
        return len(b)

    def readable(self):
        return True

# Test io.IOBase for readinto()
class FileLike(io.IOBase):

    def readinto(self, b):
        b[:] = b"\x00\x01\x02\x03"
        return len(b)

    def readable(self):
        return True

a = array.array('i', range(5))
print('A1:', a)
with FileIO() as f:
    n = f.readinto(a)
print('A2:', a)
print('n :', n)

a = array.array('i', range(5))
print('B1:', a)
with FileLike() as f:
    n = f.readinto(a)
print('B2:', a)
print('n :', n)
</
