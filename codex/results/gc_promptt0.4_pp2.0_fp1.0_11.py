import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = B(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

class C:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = C(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print
