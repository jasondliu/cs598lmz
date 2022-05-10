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
# bytearray(b'abc')
</code>
The file object has to be wrapped to support <code>readable</code>. Otherwise <code>readinto</code> would not be called at all. The <code>io</code> module was designed with this technique in mind.
A more portable implementation is not possible. You'd have to either provide an implementation for every Python implementation or link to an implementation suitable for your target platform.

