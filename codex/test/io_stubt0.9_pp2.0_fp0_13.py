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

global view

import gc
gc.collect()
gc.collect()
gc.collect()
del view
gc.collect()

