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
I also tried to use <code>io.BytesIO()</code> as the file-like object, but it doesn't work either.
<code>global view
view = b''
f = io.BufferedReader(io.BytesIO(view))
f.read(1)
del f
</code>
The <code>UnboundLocalError</code> is raised when the <code>del f</code> statement is executed.
<code>UnboundLocalError: local variable 'view' referenced before assignment
</code>
I think the variable <code>view</code> is referenced in the <code>del f</code> statement. But I don't know how to fix it.

I'm using Python 3.6.5.

