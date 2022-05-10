import weakref
# Test weakref.ref(x)

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

o = None
print(r)
print(r())

print(r2)
print(r2())

# Test weakref.ref(x, callback)

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

o = None
print(r)
print(r())

print(r2)
print(r2())

# Test weakref.proxy(x)

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()

