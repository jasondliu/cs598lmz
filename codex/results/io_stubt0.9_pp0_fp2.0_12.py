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
Why is <code>readinto</code> called twice, and why does the buffer have a length of <code>16</code> (undoubled)?
Note: It doesn't make sense to allocate or lock buffers when you aren't going to read from them. I was trying to get a non-zero sized buffer allocated that I can then use to test other modules.


A:

On this line:
<code>f = io.BufferedReader(File())
</code>
You're not just creating a <code>BufferedReader</code> instance, you're also calling <code>BufferedReader.__init__</code> on it, which does a few things.
Among other things, <code>BufferedReader.__init__</code> calls <code>BufferedReader.read</code> in order to fill its buffer.
When it does that, <code>BufferedReader</code> (the base class of <code>BufferedReader</code> objects) calls its <code>readinto</code> method.
Its <code>readinto</code> method then calls the
