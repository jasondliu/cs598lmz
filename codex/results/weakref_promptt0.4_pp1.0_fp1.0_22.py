import weakref
# Test weakref.ref()

class Foo:
    pass

class Bar:
    pass

def test_ref(ref):
    print(ref)

f = Foo()
b = Bar()

r = weakref.ref(f)
test_ref(r)

r = weakref.ref(b)
test_ref(r)

# Test weakref.WeakValueDictionary()

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

d = weakref.WeakValueDictionary()
d['foo'] = f
d['bar'] = b

print(d)

del f
del b

print(d)

# Test weakref.WeakKeyDictionary()

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

d = weakref.WeakKeyDictionary()
d[f] = 'foo'
d[b] = 'bar'

print(d)

del f
del b

print(d)
