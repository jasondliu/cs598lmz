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
That works, and I can do whatever I want with <code>view</code>.
Alas, <code>BufferedReader</code> doesn't work with <code>array</code>. To use <code>array</code>, I tried <code>MemoryIO</code>
<code>view = array.array("b")
f = io.MemoryIO(view)
f.read(1)
del f
</code>
That works until I add <code>del f</code>. Then I get a "Buffer size must not be zero" error on the <code>del f</code> line.
What am I trying to do is find a way to use <code>os.read</code> on a byte array such that I don't have to copy the bytes.
Thanks for reading.


A:

If you use <code>memoryview</code> or <code>array.array</code>, you can create a buffer that lives in memory but which is read from or written to by a file object, without copying.
<code>import io

class File(io.RawIOBase):
    def
