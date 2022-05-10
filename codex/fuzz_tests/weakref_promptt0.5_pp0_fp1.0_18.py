import weakref
# Test weakref.ref

class A(object):
    pass

a = A()
ref = weakref.ref(a)

assert ref() is a

del a

assert ref() is None

# Test weakref.WeakKeyDictionary
class A(object):
    pass

a = A()

d = weakref.WeakKeyDictionary()
d[a] = 1

assert d[a] == 1

del a

try:
    d[a]
except KeyError:
    pass
else:
    assert False

# Test weakref.WeakValueDictionary
class A(object):
    pass

a = A()

d = weakref.WeakValueDictionary()
d[1] = a

assert d[1] is a

del a

try:
    d[1]
except KeyError:
    pass
else:
    assert False

# Test weakref.WeakSet

class A(object):
    pass

a = A()

s = weakref.WeakSet()
s.add(a)

assert
