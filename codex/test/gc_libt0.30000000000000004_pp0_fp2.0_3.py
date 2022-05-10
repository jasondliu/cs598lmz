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

