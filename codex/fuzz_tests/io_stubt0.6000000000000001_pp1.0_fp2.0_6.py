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
del view
gc.collect()

# issue #29955: the weakref callback should not run until the GC is done
# with the object.

from weakref import ref

class A:
    def __del__(self):
        pass

a = A()
w = ref(a, lambda x: None)
del a
gc.collect()

# issue #29992: allocating a large block should not trigger a warning
# about the garbage collector not being able to return unused memory

from test import support

with support.check_warnings(quiet=True):
    for i in range(10):
        b = bytearray(1000000)
        del b
        gc.collect()

# issue #29993: the garbage collector should not crash when encountering
# an object with a broken tp_traverse slot

from test import support

class C:
    def __del__(self):
        pass

class D(C):
    def __init__(self):
        self.x = C()

def my_traverse(self, visit,
