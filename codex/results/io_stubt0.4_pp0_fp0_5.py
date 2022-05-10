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

def f():
    global view
    del view
    gc.collect()

f()
f()

import gc
gc.disable()

def f():
    global view
    del view
    gc.collect()

f()
f()
