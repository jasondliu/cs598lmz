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
    global view
    view[0] = 1

f()

# ____________________________________________________________

class A(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class B(A):
    pass

a = A(1)
b = B(1)

d = {a: 1, b: 2}
assert d[a] == 1
assert d[b] == 2

# ____________________________________________________________

class A(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class B(A):
    pass

a = A(1)
b = B(1)

d = {a: 1, b: 2}
