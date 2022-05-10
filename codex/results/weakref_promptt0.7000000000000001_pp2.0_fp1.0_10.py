import weakref
# Test weakref.ref() and weakref.proxy().

class C(object):
    pass

# Create a strong reference
o = C()

# Create a weak reference
r1 = weakref.ref(o)

# Create a proxy
r2 = weakref.proxy(o)

# Delete the strong reference
del o

# The weak references still work
print r1
print r2
print r1() is r2
print r1 is r2

def callback(r):
    print 'callback(%s)' % (r(),)

# Test weakref.ref() with a callback
r3 = weakref.ref(C(), callback)

# Test weakref.proxy() with a callback
r4 = weakref.proxy(C(), callback)

print 'deleting r3'
del r3

print 'deleting r4'
del r4
