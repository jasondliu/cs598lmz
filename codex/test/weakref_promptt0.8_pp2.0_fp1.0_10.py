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
