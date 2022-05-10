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
The output is:
<code>&lt;memory at 0x7f8d2b7b1c48&gt;
</code>
So, the buffer is still alive, but it is not accessible anymore.

