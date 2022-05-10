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
This sort of works, though for some reason it gives a <code>TypeError</code> if you try to read more characters at once.
<code>&lt;memory at 0x11ad1f380&gt;
&gt;&gt;&gt; view[:]
b'\r'
&gt;&gt;&gt; view[:] = b'X'
&gt;&gt;&gt; view[:]
b'X'
&gt;&gt;&gt; f.read(2)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: must be integer, not bytes
</code>


A:

Currently you are only read one byte and that byte is <code>\r</code> (a carriage return). It can be seen from <code>view[:]</code> and the fact that <code>readable()</code> method of <code>IOBase</code> which <code>RawIOBase</code> is derived from
