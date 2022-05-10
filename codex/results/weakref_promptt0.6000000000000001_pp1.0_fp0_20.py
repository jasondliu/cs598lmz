import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)

print r
print r()
print o
print o is r()
print o is r
print o is r()
