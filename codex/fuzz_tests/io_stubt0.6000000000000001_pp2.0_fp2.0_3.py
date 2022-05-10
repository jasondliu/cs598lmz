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

view.raw[0] = '\x00'

# check if the buffer is now unallocated
import gc
assert not gc.isenabled() or gc.collect() == 0

print('ok')
