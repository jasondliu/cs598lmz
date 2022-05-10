import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o = None
print(r())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)

o = None
try:
    print(p)
except ReferenceError as err:
    print(err)

# Test weakref.getweakrefcount()

class C:
    pass

o = C()

print(weakref.getweakrefcount(o))

r = weakref.ref(o)

print(weakref.getweakrefcount(o))

q = weakref.proxy(o)

print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

class C:
    pass

o = C()

print(weakref.getweakrefs(o))

r = weakref.ref(o)


