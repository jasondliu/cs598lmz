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

s = 'test'
s[1] = 'a'
print view
</code>
This shows that when the buffer is destroyed, the Python buffer is still valid.  Is there a way to make the Python buffer reference count to 0?  The only way I know to do this is to create a new buffer object.
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
view.getbuffer()
del f

s = 'test'
s[1] = 'a'
print view
</code>


A:

As far as I can see, there is no way to do this.  Calling <code>buf.getbuffer()</code> just creates a new Python buffer object.  It doesn't cause the <code>buf</code> buffer object to be deleted.
What's the use case?

