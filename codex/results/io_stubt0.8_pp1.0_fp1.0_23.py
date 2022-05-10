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
Output is <code>b''</code> (an empty byte array).  Try it online!
The problem is that the <code>BufferedReader</code> constructor does not call <code>self.raw.readable()</code>, and thus assumes that <code>self.raw</code> is a <code>RawIOBase</code> instance.  When I added <code>assert self.raw.readable(), "raw stream should be readable"</code> to the constructor, it raises an exception.

