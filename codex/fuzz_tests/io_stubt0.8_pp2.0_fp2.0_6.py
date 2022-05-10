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

class File(io.RawIOBase):
    def readinto1(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
</code>
Output is:
<code>&lt;read-write buffer ptr 0x7f3c3f7fcba0, size 1 at 0x7f3c3f7fcb10&gt;
None
</code>
The buffer object is not destroyed when the last reference to <code>f</code> is removed.
The second version <code>readinto1</code> goes away and the buffer gets destroyed. 
Is this the expected behaviour? 

