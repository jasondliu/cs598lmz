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
..and the garbage collector of course has to leave this object alive (or else <code>view</code> would become dangling). So there's no way to get rid of <code>f</code> once there's at least one <code>BufferedIOBase</code> reader around.
This is a known issue: http://bugs.python.org/issue18742
And it is why <code>io.RawIOBase</code> forces the <code>readinto</code> method to only accept writeable buffer interfaces, which have an extra variable <code>len</code> (with no connection to the function <code>len</code>) which serves as another reference for the garbage collector.
So for example, replacing <code>buf</code> with <code>memoryview(buf)</code> can help here.
Alternatively, you can just write straight to the buffer:
<code>class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b"s"
</code>
..but the documentation tells you this is supposed to append the read bytes to the buffer, not overwrite the
