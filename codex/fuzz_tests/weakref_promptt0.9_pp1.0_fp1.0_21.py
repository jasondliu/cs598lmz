import weakref
# Test weakref.reference(target, callback)
import sys
class A:
    pass
a = A()
if callback is None:
    callback = lambda ref: a.__del__(ref)
CallbackA = type(weakref.ref(a, callback))
class B:
    __slots__ = ['__weakref__']
b = B()
if callback is None:
    callback = lambda ref: b.__del__(ref)
CallbackB = type(weakref.ref(b, callback))
callback = None  # Restore default callback
PendingCallbacks = type(weakref.ref('', lambda r: print('callback!')).callbacks[0])
