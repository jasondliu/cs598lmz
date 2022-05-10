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
print view
</code>
The critical point is that a destructor that gets executed early enough. The above code works on CPython 3.3.0 64 bit (Windows).
Using <code>io.RawIOBase</code> I had to implement <code>readable</code> since that sounded like the better variant for a file-like object. But you could use a <code>io.BytesIO</code> (or a <code>io.StringIO</code>) as the basis for your file-like object.

