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

o2 = MyClass('instance2')
o3 = MyClass('instance3')

d['secondary'] = o2
d['third'] = o3

print '\nloop1:'
for o in d.items():
    print '  %s -> %s' % o

print '\nloop2:'
for o in d.values():
    print '  %s' % o

print '\nloop3:'
for o in d.keys():
    print '  %s' % o

print '\nloop4:'
for o in d.iterkeys():
    print '  %s' % o

print
