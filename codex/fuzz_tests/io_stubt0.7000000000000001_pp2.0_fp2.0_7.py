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
I see that in Python 3.8.2, <code>view</code> contains the correct data, but in PyPy 7.3.1, <code>view</code> is <code>None</code>.
I tried <code>io.BytesIO</code> instead of <code>io.BufferedReader</code>, and PyPy 7.3.1 works (as does Python 3.8.2).  I also tried <code>io.BufferedReader(io.BytesIO())</code>, and PyPy 7.3.1 works again, so it looks like the problem is that <code>io.BufferedReader</code> is not correctly sharing the wrapped file's buffer.
Is this a bug in PyPy, or am I not using the API correctly?  I can work around the problem by using <code>io.BytesIO</code> instead of <code>io.BufferedReader</code>, but it would be nice to understand why they behave differently in this case.

