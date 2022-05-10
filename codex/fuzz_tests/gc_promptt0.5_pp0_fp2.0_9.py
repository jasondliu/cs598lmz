import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

# Create a few objects that are collected
class A:
    pass

class B:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        pass

class C(A, B):
    pass

a = A()
b = B(a)
c = C()

# Create a few objects that are not collected
class D:
    pass

class E:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        pass

class F(D, E):
    pass

d = D()
e = E(d)
f = F()

# Create a weakref with a callback to an object that is collected
r = weakref.ref(c, lambda o: print("collected", o))

# There should be no output
gc.collect()
print("ok")

# Create a weakref with a callback to an object that is not collected
r = weakref.ref(f, lambda o:
