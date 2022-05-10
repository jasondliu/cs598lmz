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
del File
view[0] = 1

# This should not crash.
import io
io.BufferedReader(io.BytesIO(b""))

# Issue #23773: io.StringIO.getvalue() should not return a
# bytearray.
import io
f = io.StringIO()
f.write("abc")
assert type(f.getvalue()) is str

# Issue #23774: io.BytesIO.getvalue() should not return a
# bytearray.
import io
f = io.BytesIO()
f.write(b"abc")
assert type(f.getvalue()) is bytes

# Issue #23776: io.BufferedReader.read() should not return a
# bytearray.
import io
f = io.BufferedReader(io.BytesIO(b"abc"))
assert type(f.read()) is bytes

# Issue #23777: io.BufferedWriter.write() should not accept a
# bytearray.
import io
f = io.BufferedWriter(io.BytesIO())
try:
