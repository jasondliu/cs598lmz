import gc, weakref

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
d = weakref.WeakKeyDictionary()
d[a] = 'primary'
print(d[a])
del a
gc.collect()
print(d.get(a))

class C:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = C(10)
d = weakref.WeakKeyDictionary()
d[a] = 'primary
