import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() twice to test fix for bug #1175676.
gc.collect()
gc.collect()

def addref(obj, *args):
    if obj.wr: obj.wr()
    obj.wr = weakref.ref(obj, *args)

class MyObj:
    counter = 0                                 # total number of MyObjs
    def __init__(self):
        MyObj.counter += 1                      # increase when instantiated
        self.wr = None
        addref(self)
    __del__ = check_counters(2)                 # decrease when destroyed

iv = MyObj()
iv.wr()
del iv
assert MyObj.counter == 1                      # iv is alive until it goes out of scope

# Iv's reference count goes to zero upon return
# but local variables aren't freed until function exit.
# If a weak reference to iv is created anywhere within the frame,
# it should call iv's __del__ method at function exit.

def f():
    iv = MyObj()
    addref(iv)                                 # make it a finalizer
    addref(
