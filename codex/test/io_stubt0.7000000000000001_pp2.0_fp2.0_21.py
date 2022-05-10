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
    yield 1

class A:
    def __getattribute__(self, name):
        global L
        L += [name]
        return object.__getattribute__(self, name)

a = A()
