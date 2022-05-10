import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() + del with weakrefs to partly deallocated objects.
import weakref
class A: pass
def get_refs():
    refs = gc.get_referrers(A)
    weak = refs[0]
    return [weak() for weak in refs[1]]

a = A(); b = A()
w1 = weakref.ref(a); w2 = weakref.ref(b)
c1 = C(); c2 = C()
c1.contents = [a, b]; c2.contents = [a, b]
refs = get_refs()
if refs != [None]: print(refs)
del a; del b; gc.collect()
refs = get_refs()
if refs != [c1, c2]: print(refs)
del c1; c2.contents = None
gc.collect(); refs = get_refs()
if refs != [None, None]: print(refs)
del c2; gc.collect(); refs = get_refs()
if ref
