import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# gc.collect()
# print(gc.garbage)

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A({!r})'.format(self.name)

a = A('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
a = None
gc.collect()
print(d['primary'])

# a = A('a')
# d = weakref.WeakValueDictionary()
# d['primary'] = a
# print(d['primary'])
# d['primary'] = None
# gc.collect()
# print(d['primary'])

# a = A('a')
# d = weakref.WeakValueDictionary()
# d['primary'] = a
# print(d['primary'])
# a = None
# gc.collect()
# print(d['primary'])

# a = A('a')
# d = weakref.Weak
