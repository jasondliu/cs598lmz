import weakref
# Test weakref.ref()

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

def callback(reference):
    """Invoked when referenced object is about to be destroyed"""
    print('callback({!r})'.format(reference))

obj = Foo('an object')
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

print('making another reference to obj')
obj = Foo('another object')
r2 = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r2)
print('r2():', r2())

print('deleting obj')
del obj
print('r2():', r2())

print('making another reference to obj')
obj = Foo('another object')
r3 = weak
