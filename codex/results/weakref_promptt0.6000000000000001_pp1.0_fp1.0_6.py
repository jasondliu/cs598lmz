import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

def show(x):
    if isinstance(x, weakref.ProxyType):
        print(type(x), x)
    else:
        print(type(x), repr(x))

a = Foo()
show(a)
show(weakref.ref(a))
show(weakref.proxy(a))

b = Foo()
b.foo = a
show(b.foo)

c = weakref.ref(b.foo)
show(c)
show(c())

d = weakref.proxy(b.foo)
show(d)

e = weakref.ref(b.foo)
show(e)
show(e())

# Test weakref.WeakSet

class Foo2:
    pass

a = Foo2()
w = weakref.WeakSet([a, a, a])

b = Foo2()
w.add(b)
w.add(b)
w.add(b)

print(len(w), list(w
