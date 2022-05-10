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

view[0] = 1
print(view)
</code>
Output:
<code>&lt;memory at 0x7f4f1d8e4e08&gt;
</code>
The object here is just a memoryview, which is not a buffer in the sense of the Python buffer protocol.  It is not possible to write to it.

