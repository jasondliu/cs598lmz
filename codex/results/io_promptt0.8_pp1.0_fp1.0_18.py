import io
# Test io.RawIOBase.readinto()

import _io

# issue #17172
def segfault(file, n):
    a = bytearray(n)
    file.readinto(a)

segfault(_io.BytesIO(b'abc'), 4)

file = io.BytesIO(b'abc')
segfault(file, 4)
segfault(file, 5)
