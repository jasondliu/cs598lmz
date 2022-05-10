import weakref
# Test weakref.ref() without a callable

class C:
    pass

o = C()
r = weakref.ref(o)
print r() is o

del o
print r()

try:
    r()
except ReferenceError:
    pass
else:
    print "Expected ReferenceError"
