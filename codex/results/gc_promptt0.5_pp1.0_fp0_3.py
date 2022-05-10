import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.c = c
    c.a = a
    del a, b, c

f()
gc.collect()
# Test gc.get_objects()
class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

def f():
    a = A()
    b = B()
    c = C()
    a.b = b
    b.c = c
    c.a = a
    del a, b, c

f()
gc.collect()

l = gc.get_objects()
print len(l)
# Test gc.get_referrers()
class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

def f():

