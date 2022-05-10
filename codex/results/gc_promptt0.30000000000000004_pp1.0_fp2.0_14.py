import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

w = weakref.ref(a)

print 'collecting'
n = gc.collect()
print 'unreachable objects:', n
print 'a:',
print w() is None

w = weakref.ref(b)

print 'collecting'
n = gc.collect()
print 'unreachable objects:', n
print 'b:',
print w() is None

w = weakref.ref(c)

print 'collecting'
n = gc.collect()
print 'unreachable objects:', n
print 'c:',
print w() is None

w = weakref.ref(d)

print 'collecting'
n = gc.collect()
print 'unreachable objects:', n
print 'd:',
print w() is None

