import weakref
# Test weakref.ref()

class C(object):
    def __init__(self, a):
        self.a = a
    def g(self):
        return str(self.a)

z = C(2)
x = weakref.ref(z)
y = weakref.ref(z)
print x.g()
print y.g()

del z
print x.g()
print y.g()

try:
    print x() is None
    print y() is None
except ReferenceError:
    print "x and y went away"
