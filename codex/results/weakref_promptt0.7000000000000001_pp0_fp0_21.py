import weakref
# Test weakref.ref.__eq__()

class Foo(object):
    def __init__(self):
        self.x = 1

def eq(a, b):
    if a == b:
        print 'a == b'
    if b == a:
        print 'b == a'
    if not (a != b):
        print 'not (a != b)'
    if not (b != a):
        print 'not (b != a)'
    print

def ne(a, b):
    if a != b:
        print 'a != b'
    if b != a:
        print 'b != a'
    if not (a == b):
        print 'not (a == b)'
    if not (b == a):
        print 'not (b == a)'
    print

f = Foo()
w = weakref.ref(f)

print 'Test 1'
eq(w, w)
eq(w, f)
eq(f, w)
eq(w, 1)
eq(1, w)

print 'Test 2'
ne
