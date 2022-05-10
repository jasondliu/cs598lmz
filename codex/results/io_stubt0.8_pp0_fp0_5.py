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
view[0] = 5
</code>
I get this error:
<code>Traceback (most recent call last):
  File "C:/Python27/test.py", line 13, in &lt;module&gt;
    del f
TypeError: underlying raw stream was freed
</code>
I suspect the problem is that <code>io.BufferedReader</code> doesn't actually obtain ownership of the object, but I can't figure out how to get ownership.  I tried putting <code>view = memoryview(buf)</code> in <code>readinto()</code>, but that also raised <code>TypeError</code> when I called <code>del f</code>.
<code>view = memoryview(buf)
view[0] = 5
</code>
can be made to work, if the last line is in <code>readinto()</code>, but I want to be able to modify <code>buf</code> after Python is done using it.  So I attempted to make <code>view</code> refer to a copy of <code>buf</code> by adding <code>global
