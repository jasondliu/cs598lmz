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

view[:]                                 # What's in the buffer?
</code>

Initially, we have an empty <code>view</code> and a <code>f</code> that keeps the <code>File</code> object alive.
When we call <code>f.read(1)</code>, we're reading one byte into our <code>view</code>, because that's what the <code>File</code> object does.
When we <code>del f</code>, the <code>BufferedReader</code> destructor runs, and it needs to flush the buffer. So it calls its <code>readinto</code> method. (You can see this if you add a <code>print</code> in the <code>readinto</code> method.)

At this point, we have a <code>BufferedReader</code> object that needs to read more bytes into its internal buffer using its <code>readinto</code> method. But its internal <code>raw</code> attribute is <code>None</code>—we can see that with <code>print(f.raw)</code> before the <code
