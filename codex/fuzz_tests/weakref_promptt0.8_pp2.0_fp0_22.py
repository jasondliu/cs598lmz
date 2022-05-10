import weakref
# Test weakref.ref, weakref.ProxyType and weakref.CallableProxyType
# assignments.
print '>> Weakref to a built-in function, class object, and None'
print '   should fail'

class A:
    pass

class B:
    pass


def func():
    pass


obj = A()
obj.__dict__['a'] = 'b'

try:
    func()
except:
    pass

try:
    weakref.ref(func)
except TypeError:
    pass

try:
    weakref.ref(A)
except TypeError:
    pass

try:
    weakref.ref(None)
except TypeError:
    pass

# Instances that already have a weakref should be assignable to a
# weakref.
print '>> Weakref to an instance that already has a weakref'
print '   should succeed'

try:
    weakref.ref(obj)
except TypeError:
    pass

# Instances should be assignable to a weakref.
print '>> Weakref to an instance'

