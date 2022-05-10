import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)
o = None
print(r())

# Test weakref.proxy
o = C()
p = weakref.proxy(o)
print(p)
print(p.x)
o.x = 42
print(p.x)
o = None
try:
    print(p.x)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount
print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(p))
print(weakref.getweakrefcount(r))

# Test weakref.getweakrefs
print(weakref.getweakrefs(o))
print(weakref.getweakrefs(p))
print(weakref.getweakrefs(r))

# Test weakref.finalize
o = C()
f = weakref.finalize(o, print, 'finalized!')
print
