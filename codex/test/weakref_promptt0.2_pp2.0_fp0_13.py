import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
print(r())

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1
print(d[f])

del f
print(d)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d["foo"] = f
print(d["foo"])

del f
print(d)

# Test weakref.WeakSet()

class Foo:
    pass

f = Foo()
s = weakref.WeakSet()
s.add(f)
print(f in s)

del f
print(s)

# Test weakref.finalize()

class Foo:
    pass

f = Foo()
