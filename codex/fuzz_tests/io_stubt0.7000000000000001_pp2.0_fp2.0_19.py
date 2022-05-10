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
Output:
<code>&lt;memory at 0x01E84538&gt;
</code>
This is actually a <code>memoryview</code> object describing the buffer. <code>buf</code> itself is a memory block and <code>memoryview</code> provides read/write access to the underlying bytes. If you directly <code>print(buf)</code>, you will see the underlying bytes.

