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
print repr(view)
</code>
The output is <code>'\\x00'</code>, indicating that the buffer is filled with the 0x00 null byte. In any case, when the buffer is filled in the way described above, it ends up using the cached <code>Py_None</code> object, but whether it's cached or not is a detail of the implementation.

