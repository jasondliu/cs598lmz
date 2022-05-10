import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print repr(o), repr(r), r() is o
del o
print repr(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print repr(o), repr(p), p is o
del o
try:
    print repr(p)
except ReferenceError, e:
    print e

# Test weakref.getweakrefcount()

print weakref.getweakrefcount(o)
r = weakref.ref(o)
print weakref.getweakrefcount(o)

# Test weakref.getweakrefs()

print weakref.getweakrefs(o)
r = weakref.ref(o)
print weakref.getweakrefs(o)

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print d[o]
del o
try:
   
