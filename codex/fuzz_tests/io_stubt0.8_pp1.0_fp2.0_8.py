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
view
</code>
Output:
<code>&lt;read-write buffer object at 0x7f9e90731f10, size 1, offset 0 at 0x7f9e90731f90&gt;
</code>
So the buffer object is still alive and kicking, even after the buffer view on it was deleted. The buffer object is tied to the file object, so if the file object is still alive then the buffer object is too.

