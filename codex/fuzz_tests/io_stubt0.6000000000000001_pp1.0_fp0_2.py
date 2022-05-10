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

# ____________________________________________________________

import sys
from io import BytesIO

def test_write_into_readonly_buffer(self):
    s = BytesIO()
    b = bytearray(b"abc")
    s.write(b)
    self.assertEqual(b, b"abc")
    b[:] = b"def"
    s.seek(0)
    s.write(b)
    self.assertEqual(b, b"def")
    self.assertEqual(s.getvalue(), b"def")
    s.write(b"ghi")
    self.assertEqual(b, b"def")
    self.assertEqual(s.getvalue(), b"defghi")
    s.write(memoryview(b))
    self.assertEqual(b, b"def")
    self.assertEqual(s.getvalue(), b"defghidef")

def test_write_into_preallocated_readonly_buffer(self):
    s = BytesIO()
    b =
