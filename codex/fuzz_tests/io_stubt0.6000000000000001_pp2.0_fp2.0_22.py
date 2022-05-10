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
This code prints the first byte of the file object (which is <code>1</code>), but then, when the file object is deleted, the buffer is not cleared.
I have tried to explicitly call <code>f.close()</code>, but in that case the <code>del f</code> line raises an exception.
Is there a way to make the buffer cleared automatically, when the file object is deleted?

