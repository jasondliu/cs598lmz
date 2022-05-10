import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
print(r() is o)
print(r() is None)

o2 = C()
r2 = weakref.ref(o2)
print(r2() is o2)
print(r2() is None)

del o2
print(r2() is None)

# Test weakref.proxy()

class D:
    def __init__(self, arg):
        self.arg = arg
    def f(self):
        return self.arg

o = D(42)
p = weakref.proxy(o)
print(p.f())
print(p.arg)

o2 = D(10)
p2 = weakref.proxy(o2)
print(p2.f())
print(p2.arg)

del o2
try:
    p2.f()
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class E
