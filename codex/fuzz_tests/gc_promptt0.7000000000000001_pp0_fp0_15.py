import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by calling it several times.
# It should get rid of the objects for which gc.DEBUG_SAVEALL is set.
class Test:
    pass

def f():
    pass

class Test2:
    pass

def g():
    pass

w = weakref.ref(f)

a = Test(); b = Test(); c = Test(); d = Test(); e = Test(); f = Test(); g = Test()
h = Test(); i = Test(); j = Test(); k = Test(); l = Test(); m = Test(); n = Test()
o = Test(); p = Test(); q = Test(); r = Test(); s = Test(); t = Test(); u = Test()
v = Test(); w = Test(); x = Test(); y = Test(); z = Test()

print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(
