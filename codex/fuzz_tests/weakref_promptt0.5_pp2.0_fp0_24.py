import weakref
# Test weakref.ref(x).

class C(object):
    pass

c = C()
print repr(weakref.ref(c))

# Test weakref.ref(x, callback).

def callback(r):
    print 'callback called'

r = weakref.ref(c, callback)
print repr(r)

del c
print repr(r)

# Test weakref.proxy(x).

c = C()
print repr(weakref.proxy(c))

# Test weakref.proxy(x, callback).

p = weakref.proxy(c, callback)
print repr(p)

del c
print repr(p)
