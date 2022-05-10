import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    def __del__(self):
        print('C.__del__')

c = C()
c.x = C()
c.y = [C()]
del c
#gc.collect()
gc.garbage
# Test weakref.ref()
c = C()
c.x = C()
c.y = [C()]

def f(c):
    print('f', c)

r = weakref.ref(c, f)
del c
gc.collect()
r()
class Foo(object):
    def __init__(self, v):
        self.v = v
    def __str__(self):
        return 'Foo %s' % (self.v,)
    def __repr__(self):
        return 'Foo %s' % (self.v,)

f = Foo(1)
f
# Test weakref.WeakKeyDictionary
class A(object):
    def __init__(self):
        self.name = 'A'

a = A()
w
