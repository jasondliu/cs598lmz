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
gc.collect()
"".join(str(x) for x in view)
</code>
This can be used to implement a read-only view of a piece of memory, such as a string or a <code>bytearray</code>.

