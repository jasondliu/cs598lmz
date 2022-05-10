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
I'm not sure how to do this in Python 3. I tried the following, but got an error:
<code>import io

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
<code>AttributeError: 'memoryview' object has no attribute '__del__'
</code>


A:

The <code>memoryview</code> object is not a buffer object. It is a view on the buffer. You can't delete the memoryview, you can only delete the buffer.
The <code>memoryview</code> object is a proxy object that exposes the buffer interface, but does not own the buffer. It is created by the <code>memoryview()</code> built-in function, and it is not a subclass of the <code>memoryview</code> type.
The <code>memoryview</code
