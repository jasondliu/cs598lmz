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
a.__class__.__iter__(a)
a.send(None)
a.send(None)
a.close()
a.throw(ValueError)
del a

"""

# Translation

class A(object):

    def __init__(self):
        pass

    def __getattribute__(self, name):
        global L
        L += [name]
        return object.__getattribute__(self, name)

    def __iter__(self):
        return f()

    def send(self, param):
        print "send called with param:", param

    def close(self):
        print "close called"

    def throw(self, exception):
        print "throw called with exception:", exception

global_view = None

def test_to_target(filename):
    t = TranslationContext
