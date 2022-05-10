import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)

print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(r() is o)
print(r2() is o2)

# Test weakref.ref(obj, callback)

def callback(r):
    print("callback called with", r)

o = C()
r = weakref.ref(o, callback)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, callback)

print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(r() is o)
print(r2() is o2)

del o
del o2

print(r)
print(r
