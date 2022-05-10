import weakref
# Test weakref.ref()

class X(object):
    pass

x = X()
r = weakref.ref(x)
print(r)
print(r())

x2 = X()
r2 = weakref.ref(x2)
print(r2)
print(r2())

# Test weakref.WeakKeyDictionary

class Y(object):
    pass

y = Y()
print(y)

d = weakref.WeakKeyDictionary()
d[y] = 'foo'
print(d)
print(d[y])

del y
print(d)

# Test weakref.WeakValueDictionary

class Z(object):
    pass

z = Z()
print(z)

d = weakref.WeakValueDictionary()
d['foo'] = z
print(d)
print(d['foo'])

del z
print(d)
