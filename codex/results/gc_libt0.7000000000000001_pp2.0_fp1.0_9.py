import gc, weakref
from pprint import pprint

class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<MyClass {}>".format(self.name)

def callback(obj):
    print("{!r} deleted".format(obj))

a = MyClass("a")
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

a = MyClass("a")
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

a = MyClass("a")
d = weakref.WeakValueDictionary()
f = weakref.finalize(a, callback, a)
f.atexit = False
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d
