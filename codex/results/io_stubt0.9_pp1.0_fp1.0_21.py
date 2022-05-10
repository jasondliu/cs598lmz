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
</code>
The error you get is: <code>view = buf RuntimeError: cannot delete buffered vehicle</code>. And when you delete <code>f</code>, the internal buffer is abandoned unless you call <code>f.flush()</code>.
Edit: If you want to actually create something like this, using the default <code>BufferedIOBase</code> class does most of the work for you. Just set <code>blksize</code> to a large number, and you can read that many bytes without any copying, by returning a memoryview to <code>self._buffer</code>:
<code>from io import BufferedIOBase

class ViewIOBase(BufferedIOBase):
    def __init__(self):
        # The default buffer size is 8192, but you can set blksize to
        # a larger value and it will read that much data at a time
        super().__init__(blksize=1024)
    def readinto(self, buf):
        if not self._buffer:
            self.raw.readinto(self._buffer)
        buf[slice(0, len
