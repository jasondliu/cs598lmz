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
This works, but it's not very elegant. I'd like to avoid the global variable. Is there a better way to do this?


A:

You cannot return the buffer, since you cannot return a mutable object in Python.
You can return a copy of the buffer, but that would defeat the purpose of using a <code>BufferedReader</code> in the first place.
The global variable is the way to go.

