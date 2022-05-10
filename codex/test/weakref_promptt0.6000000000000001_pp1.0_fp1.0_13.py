import weakref
# Test weakref.ref constructor and callback function.
# If a weak reference ref has a callback, then calling ref() invokes
# the callback with the referent as its argument.

class C:
    pass

def callback(obj):
    print('callback(', obj, ')')

obj = C()
r = weakref.ref(obj, callback)

print('obj =', repr(obj))
print('reference =', repr(r))
print('r() =', repr(r()))

del obj
print('deleted obj')
print('r() =', repr(r()))
