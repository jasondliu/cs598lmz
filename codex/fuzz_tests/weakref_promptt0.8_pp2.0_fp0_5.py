import weakref
# Test weakref.reference()

class X:
    pass

def test(n):
    x = X()
    y = weakref.ref(x)
    while y() is not None:
        n -= 1
        if n <= 0:
            return
    print "weakref died prematurely!"

test(1000)
