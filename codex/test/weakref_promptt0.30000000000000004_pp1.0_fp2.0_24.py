import weakref
# Test weakref.ref() with a class that has a __del__ method.
class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('Foo.__del__(%s)' % self.name)
    def __repr__(self):
        return 'Foo(%s)' % self.name

def callback(r):
    print('callback(', r, ')')

f = Foo('f')
r = weakref.ref(f, callback)
print('created:', r)
print('created:', r())
print('deleting f')
del f
print('created:', r())

# created: <weakref at 0x7f8a4b4c4f88; to 'Foo' at 0x7f8a4b4c4e48>
# created: Foo(f)
# deleting f
# Foo.__del__(f)
# callback( <weakref at 0x7f8a4b4c4f88; dead> )
# created: None
