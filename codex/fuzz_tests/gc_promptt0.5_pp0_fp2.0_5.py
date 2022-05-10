import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass
c = C()
c.__del__ = lambda: None
del c
gc.collect()
# Test gc.collect()
class C:
    def __del__(self):
        pass
c = C()
del c
gc.collect()
# Test gc.collect()
class C:
    def __del__(self):
        pass
c = C()
c.__del__ = lambda: None
del c
gc.collect()
# Test gc.collect()
class C:
    pass
c = C()
c.__del__ = lambda: None
c = None
gc.collect()
# Test gc.collect()
class C:
    def __del__(self):
        pass
c = C()
c = None
gc.collect()
# Test gc.collect()
class C:
    def __del__(self):
        pass
c = C()
c.__del__ = lambda: None
c = None
gc.collect()
# Test gc.collect()
class C:
    pass
