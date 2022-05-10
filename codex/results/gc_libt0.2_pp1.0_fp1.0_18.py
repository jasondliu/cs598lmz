import gc, weakref

class C(object):
    pass

c = C()

def f():
    c.x = 1

f()

print c.x

del c

gc.collect()

print c.x
