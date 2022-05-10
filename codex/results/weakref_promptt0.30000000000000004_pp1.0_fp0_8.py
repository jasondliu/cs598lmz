import weakref
# Test weakref.ref(obj)

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r())

# Test weakref.ref(obj, callback)

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

# Test weakref.proxy(obj, callback)

class C:
    pass

c = C()
def callback(r):
    print("callback called with", r)

r = weakref.proxy(c, callback)
print(r)
print(r)

del c
print(r)
