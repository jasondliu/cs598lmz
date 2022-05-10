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

if hasattr(view, '__setitem__'):
    view[0] = ord('x')
</code>
Results:
<code>$ python3 buf.py
$ python3 buf.py
Segmentation fault (core dumped)

$ python buf.py
x
$ python buf.py
x
</code>
That is, in Python 2, the <code>io.BufferedReader</code> object retains a reference to the raw I/O object, but in Python 3, it doesn't.

A workaround is to explicitly hold on to the raw I/O object. This also fixes the memory leak.
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f = f.raw
del f

if hasattr(view, '__setitem__'):
    view[0] = ord('x')
</code>
Now it works in both
