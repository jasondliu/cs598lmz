import weakref
# Test weakref.ref()

class A:
    pass

a = A()
w = weakref.ref(a)
print(w)
print(w())
print(w() is a)
print(w() is None)

del a
print(w() is None)

b = A()
w2 = weakref.ref(b)
print(w2)
print(w2() is b)

print(w is w2)

print(w() is w2())

w3 = weakref.ref(A())
print(w3())
