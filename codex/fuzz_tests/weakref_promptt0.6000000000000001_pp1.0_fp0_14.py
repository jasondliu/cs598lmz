import weakref
# Test weakref.ref()
class A:
    pass
a = A()
wr = weakref.ref(a)
assert wr() is a
a = None
assert wr() is None
# Test weakref.proxy()
class A:
    pass
a = A()
wp = weakref.proxy(a)
assert wp is a
a = None
try:
    wp
except ReferenceError:
    pass
else:
    raise Exception, "should have raised ReferenceError"
# Test weakref.WeakValueDictionary()
class A:
    pass
a = A()
d = weakref.WeakValueDictionary()
d['a'] = a
assert d['a'] is a
a = None
assert d['a'] is None
# Test weakref.WeakKeyDictionary()
class A:
    pass
a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1
assert d[a] == 1
a = None
try:
    d[a]
except KeyError:
    pass
else:
    raise Exception, "should have raised KeyError"
