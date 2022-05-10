import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
o2 = r()
print(o2 is o)
del o
print(r())

# Test weakref.ref(C)

r = weakref.ref(C)
print(r)
c = r()
print(c is C)
del C
print(r())
