import weakref
# Test weakref.ref(x)

class A:
    pass

a = A()
a_ref = weakref.ref(a)

print(a_ref)
print(a_ref())

del a
print(a_ref)
print(a_ref())

a = A()
print(a_ref())

b = A()
b_ref = weakref.ref(b)
print(b_ref)
print(b_ref())

del b
print(b_ref)
print(b_ref())

b = A()
print(b_ref())

print(a_ref is b_ref)

print(a_ref() is b_ref())

a_ref_2 = weakref.ref(a)
print(a_ref_2)
print(a_ref_2())

print(a_ref is a_ref_2)

print(a_ref() is a_ref_2())

print(a_ref == a_ref_2)

print(a_ref() == a_ref_2())

