import weakref
# Test weakref.ref(obj, callback) with a callback:
# 1. check that the callback is called when the object is destroyed
# 2. check that the callback is not called when the reference is deleted
# 3. check that the callback is not called when the object is still alive

class Dummy:
    pass

class Callback:
    def __init__(self, obj):
        self.obj = obj
        self.called = 0
    def __call__(self, ref):
        self.called += 1
        self.obj.called = 1

def callback(ref):
    callback.called += 1

callback.called = 0

dummy = Dummy()
dummy.called = 0
c = Callback(dummy)
r = weakref.ref(dummy, c)

del dummy
import gc
gc.collect()

assert c.called == 1
assert dummy.called == 1

r = None
gc.collect()

assert c.called == 1
assert callback.called == 0

dummy = Dummy()
r = weakref.ref(dummy, callback
