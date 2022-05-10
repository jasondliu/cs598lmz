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
<code>b'\x00'
</code>
The docs say:
<blockquote>
<p>For a BufferedReader object, buffering is performed in the object’s read() method, which can be called repeatedly to fill the read buffer. When the read buffer is empty, the BufferedReader object’s underlying raw stream is read into the buffer. The buffer is then used to satisfy read requests on the BufferedReader object.</p>
</blockquote>
So, I was assuming that the buffer would be filled with the content of the underlying raw stream.
However, it seems that the buffer is filled with zeros.
Why is that?

