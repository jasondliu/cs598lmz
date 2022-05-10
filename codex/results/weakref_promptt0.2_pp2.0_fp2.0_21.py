import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r)
print(r())

# Test weakref.proxy()

class B:
    def __init__(self, value):
        self.value = value

b = B(42)
p = weakref.proxy(b)
print(p.value)

b.value = 43
print(p.value)

del b
try:
    print(p.value)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

print(weakref.getweakrefcount(p))

# Test weakref.getweakrefs()

print(weakref.getweakrefs(p))

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()
d[b] = 42
print(d)

del b
print(d)

# Test weakref.WeakValueDictionary
