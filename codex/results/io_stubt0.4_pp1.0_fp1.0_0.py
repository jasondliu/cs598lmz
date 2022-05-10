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

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the BufferedReader is closed.
import gc
gc.collect()
view[0] = 0

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the BufferedReader is closed.
import gc
gc.collect()
view[0] = 0

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the BufferedReader is closed.
import gc
gc.collect()
view[0] = 0

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the BufferedReader is closed.
import gc
gc.collect()
view[0] = 0

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the BufferedReader is closed.
import gc
gc.collect()
view[0] = 0

# Issue #17093: the internal buffer of the BufferedReader should be
# released when the Buff
