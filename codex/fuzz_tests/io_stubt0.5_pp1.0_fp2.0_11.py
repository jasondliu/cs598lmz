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
    return view

def g():
    del view

def h():
    import gc
    gc.collect()

import sys
sys.settrace(g)
f()
sys.settrace(h)
f()
"""

run(program)
