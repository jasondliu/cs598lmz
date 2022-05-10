import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')              # Create a reference
print('a =', a)
r = weakref.ref(a)
print('r =', r)
print('r() =', r())
print('a is r() =', a is r())

b = Foo('b')
print('b =', b)
a = None
print('a =', a)
print('r() =', r())
print('b is r() =', b is r())

c = Foo('c')
print('c =', c)
b = None
print('b =', b)
print('r() =', r())
print('c is r() =', c is r())

d = Foo('d')
print('d =', d)
c = None
print('c =', c)
print('r() =', r())
print('d is r
