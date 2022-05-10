import weakref
# Test weakref.ref(x)
class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
del o
print(r())

# Test weakref.ref(x, callback)
called = []
def callback(arg):
    called.append(arg)

o = C()
r = weakref.ref(o, callback)
print(r())
del o
print(called)

# Test weakref.proxy(x)
class D:
    pass

o = D()
p = weakref.proxy(o)
print(p.__class__)
print(p.__dict__)
print(p.__weakref__)
del o
try:
    print(p.__class__)
except ReferenceError:
    print("ReferenceError")

# Test weakref.proxy(x, callback)
called = []
def callback(arg):
    called.append(arg)

o = D()
p = weakref.proxy(o, callback)
print(p.__class__)
