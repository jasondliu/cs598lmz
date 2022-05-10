import weakref
# Test weakref.ref(instance).__call__.
class C:
    pass

x = C()
y = C()
x.a = 1
y.a = 2
z = weakref.ref(x)

x = None
y = None

print(z().a)
# Test weakref.proxy(instance).__call__.
class C:
    pass

x = C()
y = C()
x.a = 1
y.a = 2
z = weakref.proxy(x)

x = None
y = None

print(z().a)
# Test weakref.proxy(instance).__reduce__.
class C:
    pass

x = C()
y = C()
x.a = 1
y.a = 2
z = weakref.proxy(x)

x = None
y = None

print(z().a)
# Test weakref.proxy(instance).__reduce__.
class C:
    pass

x = C()
y = C()
x.a = 1
y.a = 2
z =
