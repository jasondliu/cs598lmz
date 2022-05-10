import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
del o
print(r())

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = C()
d['x'] = o
print('x' in d)
del o
print('x' in d)

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print(d[o])
del o
try:
    print(d[o])
except KeyError:
    print("KeyError")

# Test weakref.WeakSet
s = weakref.WeakSet()
o = C()
s.add(o)
print(o in s)
del o
print(o in s)

# Test weakref.finalize
o = C()
f = weakref.finalize(o, lambda o: print("finalized!"))
print(f.alive)
del o
print(
