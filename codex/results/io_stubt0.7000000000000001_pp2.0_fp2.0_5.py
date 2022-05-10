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
</code>
Output:
<code>b'\x00'
</code>
The fact that there is a single call to <code>readinto()</code> rather than multiple ones is a coincidence. If the underlying file object is buffered, you may get more than one call. If the underlying file object is unbuffered, you will get one call per read request.

