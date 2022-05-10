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

# This should not crash.
f = io.BufferedReader(File())
f.read(1)
del f
</code>
The issue is that <code>io._BufferedReader.__del__</code> doesn't call <code>self.detach()</code>, so the <code>_BufferedReader</code> instance doesn't release the <code>_BufferedIOBase</code> lock. Then, when the <code>_BufferedReader</code> instance is deallocated, the reference to the <code>view</code> buffer is released and the buffer itself is deallocated. This causes a segfault when <code>_BufferedReader.__del__</code> is called and it tries to access the buffer that was just deallocated.
The fix is to add <code>self.detach()</code> in <code>io._BufferedReader.__del__</code>:
<code>def __del__(self):
    try:
        self.detach()
    except:
        pass
</code>

