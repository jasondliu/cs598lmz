import weakref
# Test weakref.ref()
x = "abc"
t = weakref.ref(x)
print(t)
print(t())
print(t() is x)
print(t() == x)
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d['a'] = x
print(d.items())
print(d.keys())
print(d.values())
print('a' in d)
x = None
print(d.items())
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[x] = 1
print(d.items())
print(d.keys())
print(d.values())
print(x in d)
x = None
print(d.items())
# Test weakref.WeakSet
s = weakref.WeakSet()
x = "abc"
s.add(x)
print(x in s)
print(s)
x = None
print(x in s)
print(s)
# Test weakref.WeakMethod
import operator
