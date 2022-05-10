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
And it works. But I want to get rid of the global variable. So I tried the following:
<code>class File(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
    def readinto(self, buf):
        self.buf = buf
    def readable(self):
        return True

f = io.BufferedReader(File(bytearray(1)))
f.read(1)
del f
</code>
But this raises an error:
<code>TypeError: 'bytearray' object does not support item assignment
</code>
How can I get rid of the global variable?


A:

You can't assign to the <code>self.buf</code> instance attribute because it is not mutable; <code>bytearray</code> objects are not mutable.
If it is possible to change the <code>f.read(1)</code> to <code>f.readinto(bytearray(1))</code> then you can use this:
<code>class File
