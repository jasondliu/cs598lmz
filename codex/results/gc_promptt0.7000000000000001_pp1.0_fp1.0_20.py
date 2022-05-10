import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in various situations.  Note that collect() doesn't
# necessarily return the number of objects that have been freed.
print gc.collect(), gc.collect(), gc.collect()
class A:
    pass
a = A()
print gc.collect()
del a
print gc.collect()
# Exercise some edge cases of the garbage collector:
# 0.  An instance with __del__ but no __cmp__
class B(object):
    def __del__(self):
        pass
# 1.  An instance with __del__ but no __cmp__, wrapping a cycle
class C(object):
    def __init__(self):
        self.b = B()
    def __del__(self):
        pass
# 2.  A classic class with __del__ but no __cmp__, wrapping a cycle
class D:
    def __init__(self):
        self.b = B()
    def __del__(self):
        pass
# 3.  A classic class with __del__ but no __cmp__
class E:
    def __del__(self):
