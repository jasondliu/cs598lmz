import gc, weakref
import pprint

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

a = A(12)
d['primary'] = a
print(d['primary'])
d.update(secondary = a)
print(d)
print(d['primary'])
print(d['secondary'])

d.clear()
print(d)
