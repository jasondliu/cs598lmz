import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference cycle
del a
gc.collect()

# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
r = weakref.ref(a)
print(r)
print(r())
del a
gc.collect()
print(r)
print(r())

# Test weakref.finalize()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
r = weakref.finalize(a, lambda: print('finalized'))
print(r.alive)
del a
gc.
