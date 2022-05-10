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

import mmap

def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

def outer_function2(x):
    def inner_function2(y):
        return x+y
    return inner_function2

class C(object):
    def __init__(self):
        self.a = 0

    def foo(self):
        self.a += 1
        return self.a

class D(object):
    def __init__(self):
        self.a = 0

    def foo(self):
        self.a += 1
        return self.a

outer_function(1)(2)
outer_function(1)(2)
outer_function(1)(2)
outer_function(1)(2)

outer_function2(1)(2)
outer_function2(1)(2)
outer_function2(1)(2)
outer_function2(1)(2)

c = C(); c.foo()
c.foo()
c.foo()
