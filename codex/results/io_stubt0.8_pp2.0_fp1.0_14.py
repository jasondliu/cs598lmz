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
</code>
Why does the <code>BytesIO</code> buffer have <code>nbytes</code> of 20? I'd expect it to be one...


A:

<code>nbytes</code> is the length in bytes of the data stored in the buffer. The underlying <code>memoryview</code> is larger than 20 bytes, <code>nbytes</code> is only part of the data stored in the <code>memoryview</code>.

