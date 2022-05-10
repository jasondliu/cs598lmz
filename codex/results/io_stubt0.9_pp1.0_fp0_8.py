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
del File
</code>
This gives me infinite recursion, I'm guessing Python keeps trying to read into the buffer due to the <code>readable</code> call. Is there any way to emulate this behavior?
What I'm ultimately trying to achieve is have an <code>io.IOBase</code> instance that whenever read from simply returns a <code>bytearray</code> that I've set, and I want to be able to reset the array easily (hence the global variable).


A:

This implementation is better and doesn't use globals:
<code>class File(io.RawIOBase):
    def setbuffer(self, buf):
        self._view = buf
    def readinto(self, buf):
        N = len(buf)
        buf[:] = self._view[:N]
        del self._view[:N]
    def readable(self):
        return bool(getattr(self, '_view', []))
</code>
I assumed that <code>readinto</code> must read at least 1 byte. You can change this by reading only as many bytes as are
