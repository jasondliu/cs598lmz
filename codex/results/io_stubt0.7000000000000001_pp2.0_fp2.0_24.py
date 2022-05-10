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
This uses a <code>File</code> class which has a <code>readinto</code> method that sets a global variable. We then use a <code>BufferedReader</code> to wrap the <code>File</code> and read from it into a bytearray.

