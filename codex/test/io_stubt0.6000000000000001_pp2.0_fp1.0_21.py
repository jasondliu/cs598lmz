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

#print(view)

import gc
gc.collect()
print(view)
print(len(view))

for i in range(len(view)):
    print("%02x" % view[i], end='')
print()
