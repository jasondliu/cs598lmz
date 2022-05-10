import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect in a loop: the objects that survive should not be
# collectable any more.
for g in range(10):
    del c, d
    gc.collect()
    c = C()
    d = weakref.proxy(c)
c, d

# Issue #1704: crash when __del__ altered weakrefable object's class
def f():
    class A(object):
        def __del__(self):
            self.__class__ = D
    a = A()
    return weakref.ref(a)
r = f()

# Issue 3933: crash when a weakref is added to an object during its
# __del__ method
class C3933(object):
    def __init__(self):
        self.w = weakref.ref(self, lambda wr, self=self: self.check_ref(wr))

    def check_ref(self, wr):
        if wr() is not self:
            print('object has been set to None')
        else:
            print('object is still here')

def g():
    c = C39
