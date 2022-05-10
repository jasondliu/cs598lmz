import weakref
# Test weakref.ref() with a lambda

class A:
    pass

a = A()
r = weakref.ref(lambda: a)
a.b = a
del a
import gc
print(r())

gc.collect()
print(r())
