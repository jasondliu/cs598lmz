import weakref
# Test weakref.ref()

class Foo:
    pass

def callback(r):
    print('callback:', r)

f = Foo()
r = weakref.ref(f, callback)
print('r:', r)
print('f:', f)
print('r():', r())
print('deleting f')
del f
print('r():', r())

# Test weakref.WeakKeyDictionary

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1
print(d[f])
del f
print(d)

# Test weakref.WeakValueDictionary

class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d['foo'] = f
print(d['foo'])
del f
print(d)

# Test weakref.WeakSet

class Foo:
    pass

f = Foo()
s = weakref.WeakSet()
s.add(f)
print(f in s)
del f
print(
