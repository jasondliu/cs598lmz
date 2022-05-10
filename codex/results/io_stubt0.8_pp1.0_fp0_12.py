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

# on python3, we also need to close the buffer
view.close()

# test refcounting:
import gc
gc.collect()

# check that 'buf' is still alive:
if not view:
    raise RuntimeError("unexpected deallocation")
