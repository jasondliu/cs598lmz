import gc, weakref
import numpy as np

class MyClass(object):
    def __init__(self, name):
        self.name = name
        print('(Initialized: {})'.format(self.name))

    def __del__(self):
        print('(Deleted: {})'.format(self.name))

obj = MyClass('obj')
obj = 42

print('-' * 20)

a = MyClass('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']
print(d['primary'].name)

del a
gc.collect()
