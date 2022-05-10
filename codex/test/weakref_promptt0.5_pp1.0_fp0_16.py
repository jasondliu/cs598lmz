import weakref
# Test weakref.ref(object)
class C: pass
c = C()
r = weakref.ref(c)
