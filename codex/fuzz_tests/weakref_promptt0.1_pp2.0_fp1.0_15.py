import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

f = None
print(r())

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 42
print(d[f])

f = None
print(d)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d[42] = f
print(d[42])

f = None
print(d)

# Test weakref.WeakSet()

class Foo:
    pass

f = Foo()
s = weakref.WeakSet()
s.add(f)
print(f in s)

f = None
print(s)

# Test weakref.finalize()

class Foo:
    pass

f = Foo()

def callback(ref):
