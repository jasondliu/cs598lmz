import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()
# Test gc.get_referrers()
class A:
    pass

def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get_referrers()
def f():
    pass

a = A()
f()
# Test gc.get
