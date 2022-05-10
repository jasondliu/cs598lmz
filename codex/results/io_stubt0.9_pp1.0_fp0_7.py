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
buf = array.array('B', [0])
del buf
</code>
For the record, this worked, because the <code>buf</code> object was not referenced from inside the <code>File.readinto(...)</code> (it was referenced from <code>f</code>, which was not referenced from the callback). Since the object is in an unreachable state, creating a new array object with the same type and contents (i.e. 1 byte of <code>0x0</code>) does not leak, because the reference to the old buffer is gone.
[Python-ideas] and the developers have decided to fix this in 3.5.

