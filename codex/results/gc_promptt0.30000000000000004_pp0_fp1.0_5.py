import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    pass

obj = C()
obj.x = C()
obj.y = C()
obj.x.a = obj
obj.y.a = obj
obj.x.b = obj.y
obj.y.b = obj.x

w = weakref.ref(obj)
del obj
gc.collect()
print w() is None

# Test gc.garbage
class C(object):
    pass

obj = C()
obj.x = C()
obj.y = C()
obj.x.a = obj
obj.y.a = obj
obj.x.b = obj.y
obj.y.b = obj.x

w = weakref.ref(obj)
del obj
gc.collect()
print gc.garbage == [w()]

# Test gc.get_referrers()
class C(object):
    pass

obj = C()
obj.x = C()
obj.y = C()
obj.x.a = obj
obj.y.a = obj

