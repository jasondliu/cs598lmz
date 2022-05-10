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

view[0] = ord('x')
</code>
This code crashes Python with a segfault.  I'm guessing that the buffer is being deallocated before the buffer view is.  Is there a way to make this work?  Or is there a better way to read from a file into a buffer?


A:

The problem is that <code>io.BufferedReader</code> is not a context manager, so the <code>f</code> object is not being cleaned up properly.  If you add a <code>__del__</code> method to <code>File</code>, you can see that <code>f</code> is not being cleaned up, and the buffer is being deallocated before the buffer view, causing the segfault:
<code>class File(io.RawIOBase):
    def __del__(self):
        print 'deleted'
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del
