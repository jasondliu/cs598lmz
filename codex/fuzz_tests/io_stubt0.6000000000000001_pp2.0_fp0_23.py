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
I get:
<code>&lt;memory at 0x7f4fb84547c8&gt;
</code>
So, the buffer (or at least the memoryview) is still alive.

