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
This does not raise an error.  The problem is that <code>view</code> is not a ctypes array with a <code>_objects</code> field, so when the buffer is freed, the <code>_objects</code> field is dereferenced and the interpreter crashes.
To fix this, the <code>io</code> module could be fixed to copy the buffer if necessary.  Alternatively, we could patch ctypes to not crash in this case (but this would not be a good idea).

