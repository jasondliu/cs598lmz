import weakref
# Test weakref.ref

class A:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return 'A(%d)' % self.num

class B(A):
    def __str__(self):
        return 'B(%d)' % self.num

class C(A):
    def __str__(self):
        return 'C(%d)' % self.num

class D(A):
    def __str__(self):
        return 'D(%d)' % self.num

#

def checkRef(ref, cls, num):
    r = ref()
    if r == None:
        print 'passed'
    else:
        print 'failed!'
        print r

a1 = A(1)
a2 = A(2)
b1 = B(1)
b2 = B(2)
c1 = C(1)
c2 = C(2)
d1 = D(1)
d2 = D(2)

# test weakref.
