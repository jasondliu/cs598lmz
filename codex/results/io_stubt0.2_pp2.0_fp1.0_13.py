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
This prints <code>b'\x00'</code> on Python 3.6.5, but <code>b''</code> on Python 3.7.0.
I'm not sure if this is a bug or a feature, but it seems to be a change in behavior.

