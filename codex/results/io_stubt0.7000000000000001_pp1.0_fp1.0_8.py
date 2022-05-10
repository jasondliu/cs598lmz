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
view
</code>
<blockquote>
<p>ValueError: underlying buffer has been detached</p>
</blockquote>
I understand that buffers are not supposed to be copied or shared. But this particular case is confusing.


A:

<blockquote>
<p>I understand that buffers are not supposed to be copied or shared. But this particular case is confusing.</p>
</blockquote>
Actually, the rule is that buffers are not supposed to be copied or shared, and that includes keeping a reference to the object that owns them, or any object that owns that object, or any object that owns that object, or any ...
In your code, the <code>File</code> object owns the underlying buffer, so the <code>BufferedReader</code> must not keep the <code>File</code> object alive.  There are many ways that it could achieve this, but in this case it happens to achieve it by making sure that it doesn't keep any other <code>File</code> objects alive.

