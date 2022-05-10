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
</code>
This is not a real use case, but I don't know how to tell the garbage collector to release the buffer.


A:

Just use <code>del buf</code> to release the buffer.

