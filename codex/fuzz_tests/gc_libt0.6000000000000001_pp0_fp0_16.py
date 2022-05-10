import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']
print(d['primary'])

del a
print(gc.collect())
print(d['primary'])

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']
print(d['primary'])

del a
print(gc.collect())
print(d['primary'])


a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']
print(d['primary'])

del a
print(gc.collect())
print(d['primary'])
