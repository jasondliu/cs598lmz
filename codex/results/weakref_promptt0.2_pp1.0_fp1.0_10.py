import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r())

del a
print(r())

# Test weakref.proxy()

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)

del b
print(p)
