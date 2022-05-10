import gc, weakref, sys

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

# weakref.ref(a)
# d['primary'] = a
# d['primary']
# del a
# gc.collect()
# d['primary']

# d = weakref.WeakValueDictionary()
# a = A(10)
# d['primary'] = a
# d['primary']
# del a
# gc.collect()
# d['primary']

# d = weakref.WeakValueDictionary()
# a = A(10)
# d['primary'] = a
# d['primary']
# del a
# gc.collect()
# d['primary']

# d = weakref.WeakValueDictionary()
#
