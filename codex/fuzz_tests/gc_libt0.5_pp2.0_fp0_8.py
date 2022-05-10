import gc, weakref, sys

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print('printing d:', d)

del a
gc.collect()

print(d)

print(sys.getrefcount(a))
