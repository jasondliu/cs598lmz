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

import gc

gc.collect()

import array

def test(a):
    for i in range(len(a)):
        assert a[i] == i

a = array.array('b', range(10))

test(a)

del a

gc.collect()

