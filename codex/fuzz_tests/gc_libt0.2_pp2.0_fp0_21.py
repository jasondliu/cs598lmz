import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

gc.set_debug(gc.DEBUG_SAVEALL)

o = MyClass('instance')
d = weakref.WeakValueDictionary()
d['primary'] = o
print 'before, d =', d

o2 = MyClass('secondary')
d['secondary'] = o2
print 'before, d =', d

del o2
gc.collect()
print 'after, d =', d

del o
gc.collect()
print 'after, d =', d

print gc.garbage
