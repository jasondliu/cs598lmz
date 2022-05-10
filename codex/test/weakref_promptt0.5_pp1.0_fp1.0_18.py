import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()
print(f)

# weak reference to f
r = weakref.ref(f)
print(r)
print(r())

# delete f
del f

# r is still alive
print(r())

# r is dead
r = None
print(r)

# Test weakref.WeakKeyDictionary()

class Foo(object):
    pass

f = Foo()

# create a WeakKeyDictionary
d = weakref.WeakKeyDictionary()

# add f as a key
d[f] = 'bar'
print(d)

# f is alive
print(d[f])

# delete f
del f

# f is dead
print(d)
