import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect at every possible opportunity
gc.set_threshold(0)
print("\n*** test weakref GC of instance methods and callbacks ***")

def callback(arg, inst):
    print("callback", arg, "ok")

class C:
    pass

def f(arg):
    print("f", arg, "ok")

wcb = weakref.ref(callback, f)

c = C()
m = c.__eq__

wm = weakref.ref(m, callback)
del m

try:
    # will fail: callback is not callable, since f was collected
    wcb()
except AttributeError:
    pass

del f
gc.collect()

try:
    print(wm())
except ReferenceError:
    print("weak reference to instance method ok")
else:
    print("*** error *** expecting weak reference to instance method to vanish!")
del wm

c.foo = 1
wm = weakref.ref(c.foo, callback)
del c.foo
gc.collect()

try:
    print(wm
