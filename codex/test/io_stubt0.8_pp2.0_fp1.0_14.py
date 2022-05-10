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

########

from io import BytesIO
from io import RawIOBase

buffer = BytesIO()
buf = buffer.getbuffer()

print(buf.nbytes)    # 20

class NewBytesIO(RawIOBase):
    def write(self, b):
        global view
        view = b
        return len(b)

f = NewBytesIO()
print(f.write(buf))  # 20
del f

print(view)
