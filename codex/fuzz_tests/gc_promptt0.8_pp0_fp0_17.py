import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print("A.__del__")

a = A()
wr = weakref.ref(a)
print(gc.get_referents(a))
print(gc.is_tracked(a))
del a
gc.collect()
print(gc.get_count())
print(gc.get_threshold())
print(gc.get_stats())
print(gc.get_referrers(wr))
print(gc.garbage)
print(type(gc.garbage))
print(gc.is_tracked(wr))
print(gc.get_referents(wr))
print(A.__del__)

# Test gc.disable()
class B:
    def __del__(self):
        print("B.__del__")

b = B()
del b
gc.collect()
gc.disable()
gc.collect()

# Test gc.enable()
class C:
    def __del__(self):
        print("C.__del__")

