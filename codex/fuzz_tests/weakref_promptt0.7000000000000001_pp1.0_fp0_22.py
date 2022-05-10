import weakref
# Test weakref.ref
class C:
    pass
ob = C()
r = weakref.ref(ob)
print(r)
print(r())
print(ob is r())
print(r() is None)

del ob
print(r() is None)
