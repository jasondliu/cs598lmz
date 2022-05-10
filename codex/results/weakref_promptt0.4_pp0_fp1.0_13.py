import weakref
# Test weakref.ref

class C:
    pass

def callback(r):
    print('callback({!r})'.format(r))

o = C()
r = weakref.ref(o, callback)
print('o:', o)
print('ref:', r)
print('r():', r())
print('deleting o')
del o
print('r():', r())
