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
<code>b'\x00'
</code>
<code>f.read(1)</code> will read one byte from the class instance and pass it to the <code>buf</code> parameter of <code>readinto</code>. The byte is returned to <code>f.read(1)</code>. <code>f.read(1)</code> then appends that byte to its internal buffer. Then <code>f</code> goes out of scope, and the internal buffer is garbage collected. <code>view</code> is still pointing to the buffer that <code>f</code> was holding on to.

