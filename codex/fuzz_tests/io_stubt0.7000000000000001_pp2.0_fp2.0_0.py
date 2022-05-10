import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # necessary to flush the buffer
print(view)
</code>
and this is the result:
<code>b'\n'
</code>
The file-like object is just a hack to get <code>io.BufferedReader</code> to allocate a buffer of suitable size.

