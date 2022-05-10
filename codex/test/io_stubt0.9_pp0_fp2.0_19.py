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

print(bytes(view))

# view.objc_class.__str__ = lambda self: "mystr"

import gc
gc.collect()
print(gc.garbage)
