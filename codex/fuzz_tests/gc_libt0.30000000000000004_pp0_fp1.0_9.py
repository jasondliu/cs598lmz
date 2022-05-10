import gc, weakref

class A(object):
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

d['primary']

d = weakref.WeakValueDictionary()
a = A(10)
d['primary'] = a
d['primary']

a = A(20)
d['secondary'] = a
d['secondary']

del a
gc.collect()

d['primary']
d['secondary']

class B(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

b = B(10)
d = weakref.WeakKeyDictionary()
d[b] = 'foo'
d[b]

del b
gc.collect()

d

d = weak
