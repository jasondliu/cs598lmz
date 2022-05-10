import weakref
# Test weakref.ref(obj)

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
c = A('c')

# Create weak references
r1 = weakref.ref(a)
r2 = weakref.ref(b)
r3 = weakref.ref(c)

print(r1, r2, r3)
print(r1(), r2(), r3())

# Delete references
del a, b, c

print(r1(), r2(), r3())

# Delete weak references
del r1, r2, r3

# Test weakref.ref(obj, callback)

class B(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'B(%s)' % self.name

def callback(r):
    print('callback:', r)
