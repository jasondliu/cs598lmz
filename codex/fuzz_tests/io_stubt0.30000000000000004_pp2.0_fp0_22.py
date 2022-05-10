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
This prints <code>b'\x00'</code> on Python 3.3, but <code>b''</code> on Python 3.4.
I can't find anything in the docs that would indicate this is a bug, but it seems like it should be.  Is there a reason for this change?


A:

This is a bug in Python 3.4.  It has been fixed in Python 3.5.

