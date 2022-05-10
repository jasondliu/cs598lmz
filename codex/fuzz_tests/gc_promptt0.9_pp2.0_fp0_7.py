import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
a.b = A()
a.c = A()
print(gc.get_referrers(a))

del a
gc.collect()
# del a
def test_ref_dict(nreps, size):
    # Make dict
    d = dict()
    keys = list(range(size))
    for i in range(size):
        d[i] = i

    # Make references with closures.
    refs = list()
    for i in range(size):
        def get_ref(i):
            nonlocal d

            def get_value():
                return d[i]

            return get_value

        refs.append(get_ref(i))

    # GC and reassign the dict.
    gc.collect()
    d = dict()
    # Invoke the closures.
    for _ in range(nreps):
        for i in range(size):
            assert refs[i]() == keys[i]

    del refs, d

def test_ref
