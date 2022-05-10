import weakref
# Test weakref.ref()

class Foo:
    pass

def bar(obj):
    print(obj)

f = Foo()
r = weakref.ref(f, bar)
del f

print(r())

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 'bar'
print(d.data)
del f
print(d.data)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d['foo'] = f
print(d.data)
del f
print(d.data)

# Test weakref.WeakSet()

class Foo:
    pass

f = Foo()
s = weakref.WeakSet()
s.add(f)
print(s.data)
del f
print(s.data)

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo
