import weakref
# Test weakref.ref for int and float
class X(object):
    def __init__(self, a):
        self.a = a
    def __hash__(self):
        return hash(self.a)
    def __repr__(self):
        return "X(%r)" % (self.a,)

x = X(1)
y = X(2)
wr = weakref.ref(x)
print wr
print wr()
x.a = y.a
print wr()
del x
print wr()
s = str(wr)
print s, type(s)
print weakref.getweakrefcount(y), weakref.getweakrefcount(x)
wr2 = weakref.ref(y)
print wr is wr2
print wr == wr2
print wr != wr2
print wr < wr2
print wr <= wr2
print wr > wr2
print wr >= wr2
print wr2 < wr
print wr2 <= wr
print wr2 > wr
print wr2 >= wr

wr = weakref.ref(1)
wr2 = weakref.ref
