import ctypes
# Test ctypes.CFUNCTYPE for classes
class A:
    pass

def func(a):
    return a

FA = ctypes.CFUNCTYPE(A)
a = A()
f = FA(func)
f(a)
f(1) # should raise TypeError, not segfault
print 'done'
