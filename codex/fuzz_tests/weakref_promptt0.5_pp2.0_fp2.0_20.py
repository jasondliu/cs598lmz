import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r() is o)
print(r() is None)
del o
print(r() is None)

print("*"*40)

# Test callback
L = []
def f(r):
    L.append(r)
o = C()
r = weakref.ref(o, f)
print(r)
print(L)
del o
print(L)
print(L[0]())

print("*"*40)

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)
print(type(p))
print(p.__class__)
print(p.__dict__)
print(p.__weakref__ is not None)
print(p.foo)

print("*"*40)

# Test weakref.getweakrefcount() and weakref.getweakrefs()
o = C()
r = weakref.ref(o)
print
