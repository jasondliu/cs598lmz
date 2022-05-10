import weakref
# Test weakref.ref() on a type.

class C(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'C(%r, %r)' % (self.x, self.y)

def f(C):
    return weakref.ref(C)

def g(C):
    return weakref.ref(C)

c = C(1, 2)
print 'C:', c

r1 = f(c)
print 'Ref to C:', r1

c = None
print 'C deleted'

print 'Ref to C:', r1
print 'Ref to C():', r1()

print
r2 = g(r1)
print 'Ref to Ref to C:', r2

r1 = None
print 'Ref to C deleted'
print 'Ref to Ref to C:', r2
print 'Ref to Ref to C():', r2()
