import gc, weakref

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'MyClass(%s)' % self.name

gc.set_debug(gc.DEBUG_SAVEALL)

o = MyClass('instance')
wr = weakref.ref(o)
print wr()

print 'before:', gc.garbage
del o
gc.collect()
print 'after:', gc.garbage
print wr()

print 'before:', gc.garbage
del wr
gc.collect()
print 'after:', gc.garbage

gc.set_debug(0)
