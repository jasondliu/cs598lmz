import gc, weakref

class C(object):
    pass

c = C()

def f():
    c.x = 1

f()

