import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)

del a
print(r)

# Test weakref.proxy()

class A:
    pass

a = A()
p = weakref.proxy(a)
print(p)

del a
print(p)
