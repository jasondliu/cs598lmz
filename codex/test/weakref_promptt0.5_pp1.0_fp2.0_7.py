import weakref
# Test weakref.ref() with a custom class

class Foo(object):
    pass

class A(Foo):
    pass

class B(Foo):
    pass

def callback(r):
    print("callback called with", r)

r = weakref.ref(A(), callback)
print("r:", r)
print("r():", r())
print("calling")
del A
print("r():", r())
print("calling")
del B
print("r():", r())
print("exiting")
