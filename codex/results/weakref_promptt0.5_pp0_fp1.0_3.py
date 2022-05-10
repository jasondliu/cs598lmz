import weakref
# Test weakref.ref() in a class

class A:
    pass

class B(A):
    pass

a = A()
b = B()

wr1 = weakref.ref(a)
wr2 = weakref.ref(b)

print wr1() is a
print wr2() is b
print wr1() is wr2()
print wr1().__class__ is wr2().__class__

del a
del b

print wr1() is None
print wr2() is None

# Test weakref.ref() with callback

def callback(x):
    print "callback(%r)" % (x,)

a = A()
wr = weakref.ref(a, callback)
print wr() is a

del a
print wr() is None

# Test weakref.proxy() in a class

a = A()
b = B()

p1 = weakref.proxy(a)
p2 = weakref.proxy(b)

print p1 is a
print p2 is b
print p1 is p2
print p1.__class
