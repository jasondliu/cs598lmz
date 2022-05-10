import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
gc.collect()

d['primary']

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
gc.collect()

d['primary']

d = weakref.WeakValueDictionary()
d['primary'] = MyClass('a')
d['primary']

d['primary'] = MyClass('b')
d['primary']

d = weakref.WeakValueDictionary()
d['primary
