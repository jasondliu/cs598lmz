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
print(view)

# io.BytesIO
import io
from io import BytesIO
stream = BytesIO(b"abc")
print(stream.read(2))
stream.write(b"xyz")
print(stream.getvalue())

# io.StringIO
import io
from io import StringIO
stream = StringIO("abc")
print(stream.read(2))
stream.write("xyz")
print(stream.getvalue())

# io.TextIOWrapper
import io
from io import BytesIO
stream = BytesIO(b"abc\r\ndef")
print(stream.readline())
stream.seek(0)
stream = io.TextIOWrapper(stream, newline="\n")
print(stream.readline())

# io.TextIOWrapper.newlines
import io
from io import BytesIO
stream = BytesIO(b"abc\r\ndef")
stream = io.TextIOWrapper(stream)
print(stream.read())
print(stream.newlines)

