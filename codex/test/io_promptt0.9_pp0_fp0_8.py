import io
# Test io.RawIOBase
import io

class RIO(io.RawIOBase):
    def write(self, b):
        print(bytes(b))

a = RIO()
a.write(b"hello world")
a.write(b"\x00\x01\x02\x03")
# Test io.StringIO
import io
a = io.StringIO()
a.write("hello world")
print(a.getvalue())
a.write("this is a test")
print(a.getvalue())
a.seek(2,io.SEEK_SET)
print(a.readline())
print(a.read(3))
a.seek(2,io.SEEK_SET)
print(a.readline())
a.write("a\nb\nc\n")
print(a.getvalue())
print(a.readline())
print(a.readline())
print(a.readline())
# Test io.BytesIO

import io
a = io.BytesIO()
a.write(b"hello world")
