import io
# Test io.RawIOBase.write
class R(io.RawIOBase):
    def write(self, b):
        return len(b) + 10

assert R().write(b"abc") == 13

# Test io.BufferedIOBase.write
class B(io.BufferedIOBase):
    def write(self, b):
        return len(b) + 20

assert B().write(b"abc") == 23
# Test io.FileIO.write()
import os
try:
    os.remove('test.txt')
except:
    pass
f = io.FileIO('test.txt', 'w')
assert f.write(b'abc') == 3
f.close()

with open('test.txt', 'r') as f:
    assert f.read() == 'abc'

assert b'abc' == bytearray(open('test.txt', 'rb').read())

try:
    os.remove('test.txt')
except:
    pass
# Test io.StringIO.write()
s = io.StringIO()
v = s.write
