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

import gc; gc.collect()

def f():
    class A:
        def __del__(self):
            print ("A.__del__")
            del view[:]
    A()

f()
