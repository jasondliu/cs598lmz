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
It is not clear to me how the buffer is supposed to be used.  I guess I'm thinking that the buffer should be managed by the file object.  I'm also curious about how this is supposed to work in the case of a non-blocking file object.  I have never used <code>io</code> much, but I would like to understand it better.


A:

In the example you gave, buf is the buffer itself, not the object that manages it. The object that manages the buffer would be the <code>BufferedReader()</code> object.
You can see this if you use a buffer that does not support slicing:
<code>class File(io.RawIOBase):
    def readinto(self, buf):
        print(buf)
        print(buf[:])
    def readable(self):
        return True

f = io.BufferedReader(File(), 1)
f.read(1)
del f
</code>
This prints:
<code>bytearray(b'')
bytearray(b'')
</code>
