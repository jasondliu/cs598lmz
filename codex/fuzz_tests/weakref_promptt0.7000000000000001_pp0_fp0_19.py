import weakref
# Test weakref.ref()
import sys
class C: pass
o = C()
r = weakref.ref(o)
if r() is not o:
    raise TestFailed, "weakref.ref() did not return a reference to the object"
# Test weakref.proxy()
o2 = C()
p = weakref.proxy(o2)
if p.__class__ is not weakref.ProxyType:
    raise TestFailed, "weakref.proxy() did not return a proxy for the object"
# Test that the weak references have a usable repr
if repr(r).find('C') == -1:
    raise TestFailed, "weak reference repr() doesn't contain the object name"
if repr(p).find('C') == -1:
    raise TestFailed, "weak reference repr() doesn't contain the object name"

# Test weakref.getweakrefcount()
wrc = weakref.getweakrefcount
if wrc(o) != 1:
    raise TestFailed, "weakref.getweakrefcount(o) is %d, should be 1" % wrc
