import weakref
# Test weakref.ref(object)

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

del a
print(r())

a = A()
r2 = weakref.ref(a)
print(r2)
print(r2() is a)

del a
print(r2())

a = A()
r3 = weakref.ref(a)
print(r3)
print(r3() is a)

del a
print(r3())

a = A()
r4 = weakref.ref(a)
print(r4)
print(r4() is a)

del a
print(r4())

a = A()
r5 = weakref.ref(a)
print(r5)
print(r5() is a)

del a
print(r5())

a = A()
r6 = weakref.ref(a)
print(r6)
print(r6() is a)

