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
The <code>io</code> module is implemented in C, and the <code>BufferedReader</code> class is a wrapper around a file-like object.  When the <code>BufferedReader</code> is deleted, the file-like object is also deleted.  But the <code>view</code> object is still alive and well, and I can still access its data.
This seems like a bug to me.  Is it?  If not, what is the rationale for this behavior?

