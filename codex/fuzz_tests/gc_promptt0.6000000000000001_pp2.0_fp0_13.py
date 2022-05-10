import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and weakrefs.
#
print('1.')
try:
    import _weakrefset
except ImportError:
    print('SKIP')
    raise SystemExit

# Create a bunch of objects, some of which are tracked by a WeakSet.
#
print('2.')
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []

a.append(b)
b.append(c)
c.append(d)
d.append(e)
e.append(f)
f.append(g)
g.append(h)
h.append(i)


def f(x):
    return x


t = []
t.append(t)

# Create a chain of weakrefs, with a WeakSet at the end.
#
x = weakref.ref(a, f)
y = weakref.ref(x, f)
z = weakref.ref(y, f)
w = weakref.ref(z, f)


