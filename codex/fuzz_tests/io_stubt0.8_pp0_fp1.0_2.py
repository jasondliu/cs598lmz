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
Demonstration:
<code>&gt;&gt;&gt; type(view)
&lt;class 'bytearray'&gt;
&gt;&gt;&gt; view
bytearray(b'\x00')
</code>
Note that when the <code>BufferedReader</code> gets garbage collected, an internal buffer gets recycled for use on the next read.

