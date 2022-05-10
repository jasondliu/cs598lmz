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
This works fine as long as <code>f</code> is in scope.  It fails with <code>ValueError: read of closed file</code> if <code>f</code> is deleted.  I can work around this if I <code>close()</code> the file before deleting it, but this seems like a hack.
What would be the best way to get the buffer without having to worry about the lifetime of the <code>io.BufferedReader</code> object?  Or am I misunderstanding the interface to <code>io.BufferedReader</code>?


A:

<code>io.BufferedReader</code> has a <code>raw</code> attribute, which is a reference to the original <code>io.RawIOBase</code> object:
<code>f = io.BufferedReader(File())
view = f.raw
</code>

