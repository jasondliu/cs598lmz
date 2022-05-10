import weakref
# Test weakref.ref()
class C:
    pass
c = C()
r = weakref.ref(c)
print(r)
print(r())

del c
print(r)
print(r())

r = weakref.ref(42)
print(r)
