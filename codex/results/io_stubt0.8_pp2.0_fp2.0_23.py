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
yields <code>Unreferenced object deleted</code>. 
I don't understand why <code>buf</code> is unreferenceable afterwards.
What I want to do is some sort of I/O implemenation for view buffers. That is, any object that implements <code>read</code> and <code>seek</code>.

