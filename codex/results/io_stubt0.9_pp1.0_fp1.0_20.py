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
Output:
<code>&lt;read-only buffer ptr 0xXXXXXXXX, size 1 at 0x00007FF7AE629B70&gt;</code>

