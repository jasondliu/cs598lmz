import gc, weakref

class C(object):
    pass

c = C()

def f():
    print c

wr = weakref.ref(c, f)

print wr

del c

gc.collect()

print wr

print wr()
