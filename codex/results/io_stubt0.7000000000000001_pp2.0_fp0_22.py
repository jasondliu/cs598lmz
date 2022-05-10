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
del File
gc.collect()
</code>
The above code is fine on CPython, but on PyPy, it crashes with
<code>Fatal Python error: GC object already tracked
</code>
It seems that <code>BufferedReader.__init__</code> is not only creating its own buffer, but also creating a buffer view of <code>buf</code>. However, the latter is not tracked anywhere, and therefore it will be freed when the local <code>view</code> variable is freed.
It seems that PyPy has a problem with <code>PyBuffer_Check</code>. The following code does not crash:
<code>import gc
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        if not isinstance(buf, memoryview):
            view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del File
gc.collect()
</code>
Am I missing something?

