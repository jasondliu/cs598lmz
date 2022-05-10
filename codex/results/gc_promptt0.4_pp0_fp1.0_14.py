import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r(), r() is o)
del o
gc.collect()
print(r())

# Test gc.get_referrers()

a = []
b = [a]
c = [b]
d = [c]
e = [d]
f = [e]

a.append(b)
a.append(c)
a.append(d)
a.append(e)
a.append(f)

a.append(a)
b.append(b)
c.append(c)
d.append(d)
e.append(e)
f.append(f)

gc.collect()

print(gc.get_referrers(a))
print(gc.get_referrers(b))
print(gc.get_referrers(c))
print(gc.get_referrers(d))
print(gc.get_referrers(e))
print
