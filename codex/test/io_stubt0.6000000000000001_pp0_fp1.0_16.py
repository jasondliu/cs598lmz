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

# Issue #17053: reference cycles with __del__
# (also tests old-style classes)
class C:
    def __init__(self, x=None):
        self.x = x
    def __del__(self):
        pass

c = C()
c.y = c
del c

# Issue #17239: reference cycles with __del__ and __getattr__
class D(object):
    def __getattr__(self, name):
        return self
    def __del__(self):
        pass

d = D()
del d

# Issue #16367: reference cycles with __del__ and __call__
class E:
    def __call__(self, *args, **kwargs):
        pass
    def __del__(self):
        pass

e = E()
e(1)
e(2)
e(3)
del e

# Issue #17053: reference cycles with __del__
# (also tests new-style classes)
