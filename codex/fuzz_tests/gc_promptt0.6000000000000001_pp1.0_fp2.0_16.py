import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().

gc.collect()

# Create a cycle and make sure it gets collected.
l = []
l.append(l)
del l
gc.collect()

# Create a cycle and an object with a finalizer; the cycle should
# be collected before the finalizer is run.
class A:
    def __del__(self):
        print("A.__del__")
    def __repr__(self):
        return "A()"

a = A()
l = [a]
a.x = l
del l, a
gc.collect()

# Create a cycle and an object with a finalizer; the cycle should
# be collected before the finalizer is run.
class A(object):
    def __del__(self):
        print("A.__del__")
    def __repr__(self):
        return "A()"

a = A()
l = [a]
a.x = l
del l, a
gc.collect()

# Create a cycle and an object with a finalizer; the cycle should
# be collected before
