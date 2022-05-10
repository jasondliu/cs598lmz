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
This creates a <code>BufferedReader</code> object, which keeps a small amount of data read from the underlying file object in a buffer. When you read from the file object via the <code>BufferedReader</code>, the buffer is drained first, then the file object. That means you're seeing all the buffered data that was returned by the file object.
Now what you do with that data is up to you. If you just want to see what's in the buffer, use <code>bytes(view).decode()</code> (assuming it's text encoded in the default UTF8), and you'll get the text that's in it.
If you want to read again, you need to create a new <code>BufferedReader</code>:
<code>f = io.BufferedReader(File())
f.read(1)
f.seek(0)
f.read(1)
</code>

