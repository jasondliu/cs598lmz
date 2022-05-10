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
print('r() =', r())       # r() now returns None

# Test weakref.finalize()

def callback(r):
    print('callback({!r})'.format(r))

a = Foo('a')
f = weakref.finalize(a, callback, a)
print('f.alive =', f.alive)
del a
print('f.alive =', f.alive)
f()
print('f.alive =', f.alive)

# Test weakref.Weak
