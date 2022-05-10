import weakref
# Test weakref.ref

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
print(r())

# Test weakref.WeakKeyDictionary

class Foo:
    pass

f1 = Foo()
f2 = Foo()

d = weakref.WeakKeyDictionary()
d[f1] = 1
d[f2] = 2

print(d[f1])
print(d[f2])

del f1
print(d[f2])

# Test weakref.WeakValueDictionary

class Foo:
    pass

f1 = Foo()
f2 = Foo()

d = weakref.WeakValueDictionary()
d[1] = f1
d[2] = f2

print(d[1])
print(d[2])

del f1
print(d[2])

# Test weakref.WeakSet

class Foo:
    pass

f1 = Foo()
f2 = Foo()

s = weak
