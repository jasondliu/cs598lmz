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

# This is a test of the garbage collector's ability to deal with
# cyclic references.  It used to crash, but now it doesn't.

import gc

class A:
    pass

a = A()
a.a = a

gc.collect()

# This is a test of the garbage collector's ability to deal with
# cyclic references with __del__ methods.

class B:
    def __del__(self):
        pass

b = B()
b.b = b

gc.collect()

# This is a test of the garbage collector's ability to deal with
# cyclic references with __del__ methods that raise an exception.

class C:
    def __del__(self):
        raise Exception

c = C()
c.c = c

gc.collect()

# This is a test of the garbage collector's ability to deal with
# cyclic references with __del__ methods that raise an exception
# that is caught by an outer try/except.

class D:
    def __del__(self):
        raise Exception

