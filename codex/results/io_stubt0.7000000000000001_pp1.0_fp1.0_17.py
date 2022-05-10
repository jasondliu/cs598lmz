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
and it prints <code>bytearray(b'')</code>, whereas the expected behavior would be an exception.
Is this a bug in CPython, or is it anywhere specified that garbage collecting a <code>BufferedReader</code> instance invalidates the buffer given to it?
If it's the latter, I would appreciate a reference to a standard that describes this behavior.
I'm using CPython 3.4.1 on Windows 7.


A:

From the documentation for <code>_io.BufferedReader</code>:
<blockquote>
<p>The buffer may be accessed by calling <code>&lt;code&gt;getvalue()&lt;/code&gt;</code> on the buffer object.</p>
</blockquote>
That's it.  No guarantees are made regarding the lifetime of the buffer given.

