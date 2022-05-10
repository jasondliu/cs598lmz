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
view

# Don't expose the object's __dict__
class C:
    def __init__(self, x):
        self.x = x
    def __getattr__(self, name):
        if name == '__dict__':
            raise AttributeError
        return name + ' ' + self.x

def f(*args):
    return args + (C('x'),)

class C:
    def __init__(self, x):
        self.x = x
    def __getattr__(self, name):
        if name == '__dict__':
            raise AttributeError
        return name + ' ' + self.x

def f(*args):
    return args + (C('x'),)

d = {1: 1}
d.pop(0, None)

def f(a, b):
    if a and b:
        return 1
    elif a:
        # b was eliminated
        return 2
    return 3

f(1, 2)
f(0, 1)
f(1, 0)


