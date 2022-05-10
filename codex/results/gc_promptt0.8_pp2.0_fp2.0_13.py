import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
x = []
x.append(x)
print(gc.collect())
print(gc.collect())
# Test uncollectable objects
class A:
    pass

a = A()
a.x = a
del a
print(gc.collect())
# Test collect with tp_traverse != NULL
class B:
    def __getattr__(self, name):
        return self

x = B()
del x
print(gc.collect())
print(gc.collect())
# Test collection of objects with finalizers
class A:
    n = 0
    def __del__(self):
        self.n = 123
a = A()
a.x = a
del a
print(gc.collect())
print(A.n)
# Test collection of objects cyclic with finalizers
class A:
    n = 0
    def __del__(self):
        self.n = 123

a = A()
a.x = A()
a.x.x = a
del a
print(gc.collect())
print(A.n)
#
