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
However, it would be much better to use a <code>bytearray</code> instead of a <code>cffi</code> array.

