import weakref
# Test weakref.ref() on a class instance.

class Foo:
    pass

def callback(r):
    print('callback(', r, ')')

f = Foo()
r = weakref.ref(f, callback)
print('created weak reference r to', f)

print('deleting f')
del f
print('r =', r)

print('creating new instance of Foo')
f = Foo()
print('r =', r)
