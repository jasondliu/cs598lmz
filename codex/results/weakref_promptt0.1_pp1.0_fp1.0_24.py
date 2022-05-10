import weakref
# Test weakref.ref(x)

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r())

# Test weakref.ref(x, callback)

class B:
    pass

b = B()

def callback(r):
    print("callback called with", r)

r = weakref.ref(b, callback)
print(r)
print(r())

del b
print(r())

# Test weakref.proxy(x)

class C:
    pass

c = C()
p = weakref.proxy(c)
print(p)
print(p.__class__)

del c
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.proxy(x, callback)

class D:
    pass

d = D()

def callback(r):
    print("callback called with", r)

p = weakref.proxy(d, callback)
print
