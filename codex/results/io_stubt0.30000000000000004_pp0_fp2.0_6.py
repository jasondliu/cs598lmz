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
This prints <code>b'\x00'</code> on Python 3.5.1 and <code>b''</code> on Python 3.6.0.
Is this a bug in Python 3.6.0?


A:

This is a bug in 3.6.0. It has been fixed in 3.6.1.

