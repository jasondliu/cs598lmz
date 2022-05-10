import weakref
# Test weakref.ref

class Foo:
    pass

def callback(r):
    print('callback:', r)

f = Foo()
r = weakref.ref(f, callback)
print('f:', f)
print('r:', r)
print('r():', r())
print('deleting f')
del f
print('r():', r())

# Test weakref.WeakKeyDictionary

class Foo:
    pass

d = weakref.WeakKeyDictionary()
f = Foo()
d[f] = 1
print(d[f])
del f
print(d)

# Test weakref.WeakValueDictionary

class Foo:
    pass

d = weakref.WeakValueDictionary()
f = Foo()
d['foo'] = f
print(d['foo'])
del f
print(d)

# Test weakref.WeakSet

class Foo:
    pass

s = weakref.WeakSet()
f = Foo()
s.add(f)
print(f in s)
del f
print(s
