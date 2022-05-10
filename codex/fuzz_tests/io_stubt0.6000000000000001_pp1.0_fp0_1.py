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
gc.collect()
view[:] = b'x'
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
view[:] = b'y'
</code>
The code has no output, but if you run it under Valgrind, it will report a memory leak caused by the <code>x</code> and <code>y</code> values being retained.
I'm using Python 3.3 on Linux, but the same problem is present in Python 2.7.
Is there something I can do to fix this?  It's not a huge problem, but it would be nice to be able to cleanly release the memory.


A:

The problem is that the <code>BufferedReader</code> class keeps a reference to the underlying <code>RawIOBase</code> subclass in order to call <code>readinto()</code> on it.  It is not documented which instance variables it retains, but I suspect that it is retaining <code>self._raw</code>.  We can confirm this by subclassing <code>BufferedReader</code> to print out
