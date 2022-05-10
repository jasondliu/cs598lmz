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
<code>&gt;&gt;&gt;
&lt;memory at 0x101d3a3a8&gt;
</code>
I would have expected <code>print(view)</code> to throw an exception. The variable <code>view</code> is not referenced elsewhere.
I am using Python 3.6.1

