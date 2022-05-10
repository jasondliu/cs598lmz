import weakref
# Test weakref.ref behavior with weak class references.
class C(object): pass
c = C()
r = weakref.ref(c)
wc = weakref.ref(C)
d = weakref.WeakValueDictionary({'cref':r})
# Note that this will fail if wc is a strong reference,
# because the weakref module will clean up the reference
# to the class object in the WeakValueDictionary, but
# the class object will not be garbage collected because
# wc is a strong reference.
