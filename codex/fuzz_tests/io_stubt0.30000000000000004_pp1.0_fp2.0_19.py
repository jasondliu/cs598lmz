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
This prints <code>b'\x00'</code> on Python 3.7.3 and <code>b'\x00\x00\x00\x00\x00\x00\x00\x00'</code> on Python 3.8.0b1.

