import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

assert(isinstance(view, memoryview))

# Issue #23286
b = memoryview(b'abc')
result = b[0]
assert result == 97
sliceobj = slice(0, 1)
result = b[sliceobj]
assert result == b'a'
result = b[0:1]
assert result == b'a'
result = b[-1]
assert result == 99
result = b[-2:]
assert result == b'bc'
result = b[-2:2]
assert result == b'b'
result = b[-1:0]
assert result == b''

b = memoryview(b'abc')
result = b[slice(0, 1)]
assert result == b'a'
result = b[slice(0, 1, 2)]
assert result == b'a'

# Issue #19348: Test slicing crash
def f():
    s = bytearray(b'hello')
    m = memoryview(s)
    x = []
