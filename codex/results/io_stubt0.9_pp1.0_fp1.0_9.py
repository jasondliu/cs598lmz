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
view[0] = 42
</code>
When run in CPython, the object ceases to be referenced by <code>view</code> as soon as <code>del f</code> is executed, and thus the object is freed. In PyPy, the object is not freed, even after being marked as dead. Thus, <code>view[0] = 42</code> will result in a segfault.
How do I ensure that <code>f</code> is freed in PyPy? Calling <code>f.close()</code> before <code>del f</code> doesn't help.

