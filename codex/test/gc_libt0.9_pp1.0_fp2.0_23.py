import gc, weakref
from sys import getrefcount
class A:
    def __del__(self):
        print ('A.__del__')
a = A()                   # Create instance
print (getrefcount(a))    # Ref count
print (a)
d_a = weakref.ref(a)      # Proxy
print (getrefcount(a))
print (d_a)
print (d_a())
del a                 # Explicitly delete
gci = gc.get_objects() # Implicitly delete
print (gci)
print (d_a())

# example:8

import sys, weakref

class ExpensiveObject:
    def __del__(self):
        print ('(Deleting %s)' % self)

obj = ExpensiveObject()
r = weakref.ref(obj)

print ('obj:', obj)
print ('ref:', r)
print ('r():', r())

print ('deleting obj')
del obj
print ('r():', r())

