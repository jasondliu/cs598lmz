import io
# Test io.RawIOBase
class RawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'x' * n
    def close(self):
        pass
    def readinto(self, b):
        b[:] = b'x'*len(b)

# Test io.BufferedIOBase
with io.BufferedReader(RawIO()) as r:
    r.peek(3)
with io.BufferedReader(RawIO()) as r:
    r.tell()
with io.BufferedReader(RawIO()) as r:
    r.seek(3, 1)
with io.BufferedReader(RawIO()) as r:
    r.seek(3)
with io.BufferedReader(RawIO()) as r:
    r.seek(0x10, 1)
with io.BufferedReader(RawIO()) as r:
    r.read()
# The following lines would take too long on PyPy (1 min approx.)
# with io.BufferedReader(RawIO()) as r:
#     r.read1(4096)

