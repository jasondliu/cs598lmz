import weakref
# Test weakref.ref(x, callback) with a callback that raises an exception.
# The exception should not prevent the callback from being called again.

class A:
    pass

class B:
    pass

def callback(a):
    a.b.c = 1
    raise B()

a = A()
a.b = A()
a.b.c = 0
r = weakref.ref(a, callback)
del a
a = r()
print(a)
del a
a = r()
print(a)
del a
a = r()
print(a)
del a
a = r()
print(a)
