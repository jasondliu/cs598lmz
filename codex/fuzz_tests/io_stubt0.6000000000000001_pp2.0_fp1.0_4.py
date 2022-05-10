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

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
</code>
The output is:
<code>&lt;memory at 0x1a6f038&gt;
&lt;memory at 0x1a6f038&gt;
</code>
I.e. the memoryview object returned by <code>memoryview()</code> is the same as the memoryview object passed to <code>readinto()</code>.

