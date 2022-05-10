import gc, weakref

class C(object):
    pass

c = C()

def f():
    print c

w = weakref.ref(c, f)

print w
print w()

del c
gc.collect()

print w
print w()
