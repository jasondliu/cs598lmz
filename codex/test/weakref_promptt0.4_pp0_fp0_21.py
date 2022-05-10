import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')              # Create a reference
print('a =', a)
b = a                     # Increase ref. count 
print('b =', b)
c = weakref.ref(a)        # Create a weak reference
print('c =', c)
print('c() =', c())
print('deleting a')
del a                     # Decrease ref. count
print('b =', b)
print('c() =', c())

# Test weakref.WeakValueDictionary

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')              # Create a reference
print('a =', a)
d = weakref.WeakValueDictionary()
