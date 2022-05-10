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
import gc
gc.collect()
view # returns buffer with reference to GC root.
</code>
BufferedReader does not have a close method, so you cannot use this strategy generally for raw file objects. 

