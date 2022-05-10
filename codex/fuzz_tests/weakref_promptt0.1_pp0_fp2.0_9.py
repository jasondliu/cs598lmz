import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.proxy()

class D:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

o = D(10)
p = weakref.proxy(o)
print(p)
print(p.value)

o.value = 100
print(p.value)

del o
try:
    print(p.value)
except ReferenceError:
    print('ReferenceError')

# Test weakref.getweakrefcount()

class E:
    pass

a = E()
d = {1:1, 2:2, 3:3}
l = [4,
