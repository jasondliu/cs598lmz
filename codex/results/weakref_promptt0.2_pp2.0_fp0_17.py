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
print('r().name =', r().name)

a = None                  # Remove the one reference
print('a =', a)
print('r() =', r())
print('r().name =', r().name)

# Test weakref.WeakKeyDictionary()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')
b = Foo('b')
c = Foo('c')

d = weakref.WeakKeyDictionary()
d['a'] = 1

