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
view
</code>
This is the same issue as issue #13203 in the Python bug tracker.


A:

According to the reference documentation, <code>BufferedReader.readinto</code> will fall back to calling <code>read</code> if it has no implementation of its own.
However, as of Python 3.5, there is no implementation of <code>BufferedReader.readinto</code> in <code>io.py</code>. There's only a definition that does this fallback:
<code>def readinto(self, b):
    """Read up to len(b) bytes into b.

    Returns number of bytes read (0 for EOF), or None if the object
    is set not to block and has no data to read.
    """
    if self.raw.readable():
        return self.raw.readinto(b)
    self.fill()
    return self.buffer.readinto(b)
</code>
As you can see, <code>self.raw.readable()</code> will be evaluated before <code>self.fill()</code> is called.
