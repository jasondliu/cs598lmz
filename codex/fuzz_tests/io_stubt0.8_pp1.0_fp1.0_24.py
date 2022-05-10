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
As you can see, <code>del f</code> is called only after <code>view</code> is referenced, so the created object should still exist.
However, running this code shows that <code>del</code> has been called:
<code>$ python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 12, in &lt;module&gt;
    view
UnboundLocalError: local variable 'view' referenced before assignment
</code>
Why does this happen?
Note: I'm aware that the error doesn't happen when you create a <code>BufferedReader</code> from a file object, so it must have to do with the <code>File</code> class.

