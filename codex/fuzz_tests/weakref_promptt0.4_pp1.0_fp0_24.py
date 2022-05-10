import weakref
# Test weakref.ref(object)
class C: pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
# Test weakref.ref(object, callback)
def callback(r):
    print("callback called with", r)
    raise SystemExit
r = weakref.ref(o, callback)
print(r)
print(r())
print(r() is o)
del o
print(r)
print(r())
print(r() is None)
# Test weakref.ref(object, callback) with exception in callback
def callback(r):
    print("callback called with", r)
    raise Exception
r = weakref.ref(o, callback)
print(r)
print(r())
print(r() is o)
del o
print(r)
print(r())
print(r() is None)
# Test weakref.ref(object, callback) with exception in callback
def callback(r):
    print("callback called with", r)
    raise SystemExit
r = weakref.
