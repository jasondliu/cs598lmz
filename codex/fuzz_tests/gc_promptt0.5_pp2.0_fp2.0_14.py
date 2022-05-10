import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, arg):
        self.arg = arg
    def __del__(self):
        print("A.__del__")

a = A(1)
print("a =", a)
print("collecting...")
n = gc.collect()
print("unreachable objects:", n)
print("a =", a)

a = A(2)
print("a =", a)
del a
print("collecting...")
n = gc.collect()
print("unreachable objects:", n)

a = A(3)
print("a =", a)
wr = weakref.ref(a)
print("wr =", wr)
print("collecting...")
n = gc.collect()
print("unreachable objects:", n)
print("wr =", wr)
print("a =", a)
del a
print("collecting...")
n = gc.collect()
print("unreachable objects:", n)
print("wr =", wr)
# Test g
