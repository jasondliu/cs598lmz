import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on objects that can be collected.
# This is a good test for long object chains.

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '<A %d>' % self.value

a = A(1)
w = weakref.ref(a)
print('exists before:', w())
del a
print('exists after:', w())
gc.collect()
gc.collect()
print('exists after:', w())

print('*** test gc.collect() on uncollectable objects ***')
# Test gc.collect() on objects that can't be collected.

class C:
    # avoid __del__
    def __init__(self):
        pass

class B:
    def __init__(self):
        self.c = C()

b = B()
w = weakref.ref(b)
print('exists before:', w())
del b
print('exists after:', w())
gc.collect()
print('
