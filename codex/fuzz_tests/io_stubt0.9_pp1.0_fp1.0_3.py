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
import gc; gc.collect()
print view
</code>
<code>readinto</code> does not need to return anything because when it succeeds, <code>buf</code> will be populated with the data read in.

