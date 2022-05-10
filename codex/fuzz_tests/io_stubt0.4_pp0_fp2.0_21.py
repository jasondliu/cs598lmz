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
This works fine, but I would like to make <code>view</code> a <code>bytearray</code>, so I can do <code>view[0] = 42</code> and have that change the value in the buffer.  But I can't figure out how to do that.  I tried this:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = bytearray(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

print(view)
view[0] = 42
print(view)
</code>
But this throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 16, in &lt;module&gt;
    view[0] = 42
TypeError: 'bytearray' object does not support item assignment
</code>
So how do I make <code>
