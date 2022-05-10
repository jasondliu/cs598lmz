import weakref
# Test weakref.ref(obj)
import weakref

class A:
    pass

a = A()
r = weakref.ref(a)
a.x = 1
print(r().x)
del a
print(r())

# Test weakref.ref(obj, callback)
import weakref

class A:
    pass

a = A()
a.x = 1

def cb(wr):
    print(wr().x)

r = weakref.ref(a, cb)
del a

# Test weakref.proxy(obj)
import weakref

class A:
    pass

a = A()
a.x = 1
p = weakref.proxy(a)
print(p.x)
del a
try:
    print(p.x)
except ReferenceError:
    print("ReferenceError")

# Test weakref.proxy(obj, callback)
import weakref

class A:
    pass

a = A()
a.x = 1

def cb(wr):
    print(wr().x)


