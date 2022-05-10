import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
gc.collect()
gc.collect()
class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name
    def __del__(self):
        print 'going to be collected:', self
        gc.collect()
        print 'collected:', self
a = A("one")
b = A("two")
c = A("three")
l = [a, b, c]
del a, b, c
gc.garbage.extend(l)
gc.collect()
# Test gc.set_threshold()
class A:
    pass
def foo():
    print len(gc.get_objects())
    gc.collect()
gc.callbacks.append(foo)
gc.set_threshold(1)
a = A()
del a
gc.collect()

