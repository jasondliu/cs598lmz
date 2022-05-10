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
So the <code>readinto</code> method seems to work, but I'm not sure if it's possible to get the <code>read</code> method to work.


A:

I'm not sure what you mean by "get the read method to work".
The <code>read()</code> method of <code>io.RawIOBase</code> calls <code>readinto()</code> with a newly allocated buffer. The <code>readinto()</code> method of your <code>File</code> class replaces the global <code>view</code> with that buffer, and returns the number of bytes it read.
So, the <code>read()</code> method of <code>io.RawIOBase</code> returns the number of bytes it read, and the global <code>view</code> is the buffer it read into.

