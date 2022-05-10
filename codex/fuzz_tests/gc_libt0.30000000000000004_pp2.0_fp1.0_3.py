import gc, weakref
from pprint import pprint

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
gc.collect()

pprint(d.data)

d['primary']

class B:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = B(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
gc.collect()

pprint(d.data)

d['primary']

class C:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = C(10)
d = weak
