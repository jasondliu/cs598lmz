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

view[0] = ord('a')

# test that the base object is not finalized
import gc
collectable = []
collectable.append(view)
gc.collect()
print view[0]
del collectable
gc.collect()
print view[0]

# test that an internal buffer is released
view = None
gc.collect()

# test that the base object is finalized
view = None
gc.collect()
print

# test that the base object is not finalized
view = None
collectable = []
collectable.append(view)
gc.collect()
print view
del collectable
gc.collect()
print view

# test that an internal buffer is released
view = None
gc.collect()

# test that the base object is finalized
view = None
gc.collect()



# Test that readinto() returns a 0-sized buffer if the base object is finalized.
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True


