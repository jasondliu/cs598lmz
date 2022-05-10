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
<code>&gt;&gt;&gt; print(view)
b'\x00'
</code>
The garbage collector is not involved in this.

