import weakref
# Test weakref.ref() with weakref.finalize()

import weakref

class Foo:
    pass

f = Foo()
r = weakref.ref(f)

def callback(r):
    print('callback(%r)' % r)

f = weakref.finalize(f, callback, r)

print(f.alive)
del f
print(r())
print(r())
