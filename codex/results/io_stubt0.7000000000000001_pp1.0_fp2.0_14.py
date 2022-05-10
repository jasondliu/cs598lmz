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
view[0] = 42
</code>
I get the following error:
<code>TypeError: readinto() argument 1 must be array.array, not bytearray
</code>
Why <code>bytearray</code> is not an array? 
Is there any way to get a <code>bytearray</code> back from a <code>BufferedReader</code>?


A:

There are probably a few ways to do this, but the one I'm most familiar with is to use the <code>memoryview</code> class:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

buf = bytearray(1)
mv = memoryview(buf)
mv[0] = 42
</code>

