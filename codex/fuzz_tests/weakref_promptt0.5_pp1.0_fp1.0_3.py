import weakref
# Test weakref.ref()
class A: pass
a = A()
b = weakref.ref(a)
print(b)

# Test weakref.getweakrefcount()
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
print(weakref.getweakrefs(a))

# Test weakref.proxy()
class B: pass
c = B()
d = weakref.proxy(c)
print(d)

# Test weakref.finalize()
class C: pass
e = C()
def callback(arg):
    print("callback called")
f = weakref.finalize(e, callback, 'arg')
print(f)

# Test weakref.WeakKeyDictionary()
class D: pass
g = D()
h = D()
w = weakref.WeakKeyDictionary()
w[g] = 'g'
w[h] = 'h'
print(w)

# Test weakref.WeakValueDictionary()
class E: pass
i = E()
j = E()
w =
