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
sys.getrefcount(view)
</code>
In Python 3.4.2 it returns 2.
In Python 3.5.0 it returns 1.
This is a problem for me because I'm using Python 3.4.2, but I want to be able to use the <code>readable()</code> method of an <code>io.RawIOBase</code>-derived class.

