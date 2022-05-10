import weakref
import gc

class Widget(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Widget({!r})'.format(self.name)

a = Widget('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
