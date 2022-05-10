import gc, weakref, sys

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print('d["primary"] ->', d['primary'])
del a
gc.collect()
print('d["primary"] ->', d['primary'])

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = B(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary'].value = 20
print('d["primary"] ->', d['primary'])
del a
gc.collect()
print('d["primary"] ->', d['primary'])
