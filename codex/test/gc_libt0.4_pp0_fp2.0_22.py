import gc, weakref

class C(object):
    pass

c = C()

def f():
    print(c)

w = weakref.ref(c, f)

c = None

gc.collect()

print(w)
