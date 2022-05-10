import weakref
# Test weakref.ref
class C(object):
    pass

c = C()
wr = weakref.ref(c)
assert wr() is c
del c
assert wr() is None
# Test weakref.proxy
class C(object):
    pass

c = C()
wr = weakref.proxy(c)
assert wr is c
del c
try:
    wr
except ReferenceError:
    pass
else:
    raise Exception, "not ReferenceError"
# Test weakref.WeakKeyDictionary
class C(object):
    pass

c = C()
d = weakref.WeakKeyDictionary()
d[c] = 1
assert d[c] == 1
del c
try:
    d[c]
except KeyError:
    pass
else:
    raise Exception, "not KeyError"
# Test weakref.WeakValueDictionary
class C(object):
    pass

c = C()
d = weakref.WeakValueDictionary()
d[1] = c
assert d[1] is c
del c
try:
    d[1]

