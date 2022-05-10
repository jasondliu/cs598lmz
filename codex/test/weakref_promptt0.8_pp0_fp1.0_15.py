import weakref
# Test weakref.ref with __eq__.

class C(object):
    def __init__(self, arg):
        self.x = arg
    def __repr__(self):
        return "<C %s>" % self.x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

a = C('a')
b = C('b')
c = C('c')
d = C('d')
e = C('e')
f = C('f')
g = C('g')
w = weakref.ref(e)

dct = {}

for i in range(5):
    dct[C(i)] = 1

del i

# Make sure new objects compare as equal to old ones.

dct[C('c')] = 2
dct[C(3)] = 3
dct[C(-2)] = 4
