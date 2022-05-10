import weakref
# Test weakref.ref()
class A:
    pass
a = A()
wr = weakref.ref(a)
print isinstance(wr, weakref.ReferenceType)
print wr() is a
print a is None
print wr() is None
# Test weakref.WeakKeyDictionary
class A:
    pass
a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1
print len(d)
a = None
print len(d)
# Test weakref.WeakValueDictionary
class A:
    pass
a = A()
d = weakref.WeakValueDictionary()
d[1] = a
print len(d)
a = None
print len(d)
# Test weakref.WeakSet
class A:
    pass
a = A()
s = weakref.WeakSet()
s.add(a)
print len(s)
a = None
print len(s)
# Test weakref.proxy()
class A:
    pass
a = A()
p = weakref.proxy(a)
print isinstance(p, weak
