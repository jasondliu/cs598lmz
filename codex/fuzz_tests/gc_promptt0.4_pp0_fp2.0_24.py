import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
print(wr)
del f
gc.collect()
print(wr)

# Test gc.garbage

class A:
    def __del__(self):
        print("A.__del__")

class B(A):
    def __del__(self):
        print("B.__del__")
        A.__del__(self)

class C(B):
    def __del__(self):
        print("C.__del__")
        B.__del__(self)

a = A()
b = B()
c = C()
gc.garbage.append(a)
gc.garbage.append(b)
gc.garbage.append(c)
gc.collect()
print(gc.garbage)
