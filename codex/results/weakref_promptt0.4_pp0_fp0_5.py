import weakref
# Test weakref.ref(x) == weakref.ref(x)
#
# Note: This test is not in the test suite because it doesn't work
# on all platforms.

class Foo:
    pass

f1 = Foo()
f2 = Foo()

r1 = weakref.ref(f1)
r2 = weakref.ref(f1)
r3 = weakref.ref(f2)

if r1 == r2:
    print "OK"
else:
    print "r1 != r2"

if r1 != r3:
    print "OK"
else:
    print "r1 == r3"
