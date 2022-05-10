import weakref
# Test weakref.ref()

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

def callback(r):
    print("callback", r)

r3 = weakref.ref(o, callback)

print("deleting o")
del o
print("deleting o2")
del o2

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

def callback(p):
    print("callback", p)

p3 = weakref.proxy(o, callback)

print("deleting o")
del o
print("deleting o2")
del o2

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweak
