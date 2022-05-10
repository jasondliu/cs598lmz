import weakref
# Test weakref.ref(obj)

class A:
    pass

a = A()
a_ref = weakref.ref(a)
print(a_ref)
print(a_ref())

del a
print(a_ref)
print(a_ref())

# Test weakref.proxy(obj)

a = A()
a_proxy = weakref.proxy(a)
print(a_proxy)
print(a_proxy.__class__)

del a
print(a_proxy)
