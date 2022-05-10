import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a cyclic list.
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)

a = A(1)
b = A(2)
c = A(3)
a.next = b
b.next = c
c.next = a
wr = weakref.ref(a)
del a, b, c
gc.collect()
print(wr())

# Test gc.collect() with a weakref to an instance.
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)

a = A(1)
wr = weakref.ref(a)
del a
gc.collect()
print(wr())

# Test gc.collect() with a weakref to an instance which has a __del__ method.
class A:
    def __init__(self, value):
        self.value = value

