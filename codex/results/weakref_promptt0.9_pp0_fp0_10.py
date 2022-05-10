import weakref
# Test weakref.ref_iter with various cyclic structures.
class Foo:
    pass

class Bar:
    pass

class Empty:
    pass
# Create weakrefs to the instances.
L = [Bar(), Empty(), Foo()]
weak_L = [weakref.ref(l) for l in L]
D = {'one': Bar(), 'two': Empty(), 'three': Foo()}
weak_D = {}
for k, v in D.items():
    weak_D[k] = weakref.ref(v)
try:
    frozenset
except NameError:
    pass
else:
    F = frozenset([Bar(), Empty(), Foo()])
    weak_F = weakref.ref(F)
# Do the iteration
it = weakref.ref_iterator(D)
for wobj in it:
    obj = wobj()
    if obj is None:
        continue
    for w in weak_D:
        if weak_D[w]() is obj:
            bad.append('D[%r] is dead and weakref_data %r' % (
