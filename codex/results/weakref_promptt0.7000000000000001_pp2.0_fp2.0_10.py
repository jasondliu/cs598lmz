import weakref
# Test weakref.ref for objects which (1) can be weakly referenced, and (2)
# have a __del__ method which raises an exception when called.  The
# reference must become invalid when the referent is deleted.

class C:
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback(self)
        raise ValueError

def callback(ref):
    print "callback", ref
    global n_callback
    n_callback += 1

# The first time the reference is created and destroyed, there is a
# RuntimeError because the exception in __del__ is not caught.  __del__
# is called a second time when the exception unwinds the stack, and this
# time the exception is caught and turns the reference into a dead one.

for i in range(2):
    n_callback = 0
    c = C(callback)
    x = weakref.ref(c)
    del c
    gc.collect()
    print n_callback
    if n_callback == 2:
        break
else:

