import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.c = a
a.b.d = a.b
del a
gc.collect()
gc.collect()
gc.collect()

# Test gc.garbage
class MyClass:
    def __del__(self):
        print 'MyClass.__del__'

gc.garbage.append(MyClass())
gc.garbage.append(MyClass())
gc.collect()

gc.garbage[:] = []
gc.collect()

# Test cyclic gc
# XXX: PyPy's GC doesn't support it, so just test that it doesn't crash
class MyClass:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<MyClass %s>' % (self.name,)
    def __del__(self):
        print 'MyClass.__del__', self.name

o = MyClass('o')
l = [o]
d = {'
