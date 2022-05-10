import weakref
# Test weakref.ref(subclass_of_weakrefable)
# Bug #540359

class C(weakref.ref):
    pass

def callback(obj):
    pass

r = C(callback, {})
r()
print 'ok'
