import weakref
# Test weakref.ref().

def f(x):
    return x * x

def g(x, y):
    return x + y

def h(x):
    return repr(x)

def show(message, r):
    print message, ":", r(),

    o = r()
    if o is not None:
        print o.__class__.__name__,

    print
    return r

r = weakref.ref(8)
show("numeric", r)
r = show("string", weakref.ref("Hello"))
r = show("tuple", weakref.ref((1, 2, 3)))
r = show("list", weakref.ref([4, 5, 6]))
r = show("dict", weakref.ref({'one': 1, 'two': 2}))
r = show("function", weakref.ref(f))
r = show("unbound method", weakref.ref(list.append))
r = show("bound method", weakref.ref(r().append))

try:
    import thread
    r = show("lock",
