import weakref
# Test weakref.ref()
import gc

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
gc.collect()
print(r())

# Test weakref.proxy()
import weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
d['primary']

# Test weakref.finalize()
import weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
ref = weakref.finalize(a, lambda: print('finalized'))
ref.alive

del a
ref.alive

# Test weakref.WeakKeyD
