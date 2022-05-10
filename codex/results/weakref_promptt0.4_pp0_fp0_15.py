import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r)
print(r())

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())
print(r)

a = A()
print(r())
print(r)

del a
print(r())

