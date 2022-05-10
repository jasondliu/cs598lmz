import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

def callback(r):
    print('callback(', r, ')')

f = Foo('f')
r = weakref.ref(f, callback)
print('created object:', f)
print('created weak reference:', r)
print('r():', r())
print('deleting f')
del f
print('r():', r())

# created object: Foo('f')
# created weak reference: <weakref at 0x10b2a3e08; to 'Foo' at 0x10b2a3d68>
# r(): Foo('f')
# deleting f
# callback( <weakref at 0x10b2a3e08; dead> )
# r(): None

# Test weakref.ref(<builtin>)

class Foo:
    def __init__(self, name):
        self.name = name
   
