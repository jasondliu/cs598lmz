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


def foo():
    raise RuntimeError

def bar():
    try:
        foo()
    except RuntimeError:
        return "bar"
    return "bar2"

def baz():
    try:
        bar()
    except RuntimeError:
        return "baz"
    return "baz2"

print (baz())

import io

class MyIO(io.IOBase):
    def readable(self):
        return True
    def readinto(self, buf):
        global view
        view = buf

f = io.BufferedReader(MyIO())
print (f.read(1))
del f

def f1():
    return 1

def f2():
    @f1
    def g():
        pass

print (f2())
