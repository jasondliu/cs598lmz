import ctypes
ctypes.cast(0, ctypes.py_object).value
sys.getrefcount(0)
a = sys.getrefcount(0)
b = sys.getrefcount(None)
c = sys.getrefcount(Ellipsis)
d = sys.getrefcount(1)
(a, b, c, d)

# A circular reference.
x = []
x.append(x)

# Now create a cycle involving different types.
x = []
y = {}
x.append(y)
y['x'] = x

# Python doesn't collect the cycle.
import gc
gc.collect()

# Python doesn't collect the cycle.
import gc
gc.collect()

# But if we create references to the objects in the
# cycle from outside the cycle, it can collect it.
x = []
y = {}
x.append(y)
y['x'] = x
del x
del y
gc.collect()

# Python has a cycle detector.
import gc
gc.set_debug(gc.DEBUG_SAVEALL)
x = []
