import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
st = time.time()
while time.time() - st < 5:
    l = [weakref.ref(j) for j in range(100)]
    gc.collect()
    print gc.collect()

# Test gc.get_referents
class A:
    pass

a = A()
b = A()
l = [a]
d = {1:a, 2:b}
s = set([a])

print gc.get_referents(a) == [l, d, s]
print gc.get_referents(b) == [d]
print gc.get_referents(l) == []
print gc.get_referents(d) == []
print gc.get_referents(s) == []

class B:
    pass

b1 = B()
b2 = B()
b3 = B()
l = [b1]
l.append(b1)
d = {1:b1, 2:b2}
s = set([b1,
