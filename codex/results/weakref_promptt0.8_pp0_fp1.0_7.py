import weakref
# Test weakref.ref() and weakref.proxy()

class D:
    pass

class C:
    pass

class B(C):
    pass

class A(B, D):
    pass

def test_ref(a):
    print "Should not be dead:"
    r = weakref.ref(a)
    rp = weakref.proxy(a)
    print r()
    print rp
    print rp.__class__

    print "Should be dead:"
    del a
    try:
        print r()
    except ReferenceError:
        print "ReferenceError"
    try:
        print rp
    except ReferenceError:
        print "ReferenceError"
    try:
        print rp.__class__
    except ReferenceError:
        print "ReferenceError"

print "Testing class A"
test_ref(A())
print "Testing class B"
test_ref(B())
print "Testing class C"
test_ref(C())
print "Testing class D"
test_ref(D())

print "Testing int"
test_ref
