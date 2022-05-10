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
In fact, Python 2.6.2 even accepts the above code! In 2.7, however, the <code>RawIOBase</code> implementation of <code>readinto()</code> explicitly checks to see whether <code>self</code> is a class type, and raises a TypeError if it is. Apparently the Python 2.7 developers find it an error to instantiate a <code>RawIOBase</code> subclass that is a class type rather than a true instance.
I'm not sure why this should be, unless they are trying to prevent the possibility of buffer overflow. It does seem like <code>RawIOBase</code> should be more flexible about allowing classes to be instantiated for it, since it's not doing anything with <code>self</code>, and it is not a required method anyway.

