import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    p = ctypes.POINTER(x)

def check(l, test):
    for i in range(len(l)):
        assert l[i] == i
        assert test(i)

l = range(25)
print l
check(l, lambda x: x in l)

class A(object):
    def __init__(self, v):
        self.v = v
    def __repr__(self):
        return 'A(%d)' % self.v
    def __eq__(self, other):
        return self.v == other.v

a = A(4)
b = A(4)
c = A(4)
def checka(l):
    for i in range(len(l)):
        assert l[i] == a
        assert i != a
        l[i] = b
        l[i] = a

l = [a] * 25
print l
checka(l)
check(l, lambda x: l[x] == a)

l
