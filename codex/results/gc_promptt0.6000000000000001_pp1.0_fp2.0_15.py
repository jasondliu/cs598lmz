import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    def __del__(self):
        print("C.__del__")

c1 = C()
weakref.ref(c1)
gc.collect()
c1 = None
gc.collect()
# Test __del__
class C(object):
    def __del__(self):
        print("C.__del__")

c1 = C()
c2 = c1
c1 = c2
del c1
del c2
gc.collect()
# Test weakref
class C(object):
    def __del__(self):
        print("C.__del__")

c1 = C()
ref = weakref.ref(c1)
assert ref() is c1
weakref.ref(c1)
c1 = None
gc.collect()
assert ref() is None
# Test gc.garbage
class C(object):
    def __del__(self):
        print("C.__del__")

c1 = C()
weakref.ref(c1)
c1 = None

