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
However, I don't understand how this does anything useful. The <code>readinto</code> method doesn't return the number of bytes written to <code>buf</code>, so I don't see how this can work.
What am I missing?

