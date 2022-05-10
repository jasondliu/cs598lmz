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

# This used to crash
view[0] = b'x'
</code>
The issue is that <code>view</code> is a <code>memoryview</code> object, and the <code>memoryview</code> object is not a reference to the underlying buffer, but a view of it.
The <code>memoryview</code> object is a wrapper around the buffer, and the <code>memoryview</code> object is a reference to the buffer, so when you delete the <code>BufferedReader</code> object, the <code>memoryview</code> object is still alive.
When you delete the <code>BufferedReader</code> object, the buffer is deallocated, and the <code>memoryview</code> object is left with a dangling pointer.
When you try to access the <code>memoryview</code> object, it tries to access the buffer, and you get a segfault.

If you want to keep a reference to the buffer, you need to keep a reference to the <code>memoryview</code> object, not the buffer itself.

