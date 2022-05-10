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
print("after:", view)
</code>
If you run this, you'll see that the <code>view</code> is still there after the <code>io.BufferedReader</code> object is deleted.
So, how do I get the <code>io.BufferedReader</code> to release the <code>memoryview</code>?

