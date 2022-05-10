import weakref
# Test weakref.ref

def foo():
    global a
    a = {'hello': 'world'}
    b = weakref.ref(a)
    return b

b = foo()

print(b() is a)

# delete original dictionary
del a
print(b() is None)
del b
# Test a weakref correctly cleans up a list slot

def foo():
    l = []
    c = weakref.ref(l, lambda wr: l[0] == 1)
    l.append(1)
    return c

print(foo()() is None)
# Test a weakref correctly cleans up a dictionary slot

def foo():
    o = {}
    c = weakref.ref(o, lambda wr: o['hello'] == 'world')
    o['hello'] = 'world'
    return c

print(foo()() is None)
# Test a weakref correctly cleans up a dict key
#
# Note: this doesn't work so well if we create multiple weakrefs to the
# same key, since we don't keep track of how many weak references there

