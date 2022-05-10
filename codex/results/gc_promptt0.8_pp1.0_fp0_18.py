import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when running the garbage collector recursively by
# calling back into Python for a hash table resize.
print('gc.collect() with recursive hash table resize')

class C:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return 'C(%r)' % (self.n,)

def boom():
    c = C(1)
    d = {1: c, 2: c, 3: c, 4: c}
    print('cycle created')
    gc.collect()
    d[5] = c
    print('dict resized:', d)
    print('cycle should be unreachable now')

boom()
# Test gc.get_referrers() when running the garbage collector recursively.
print('gc.get_referrers() with recursive hash table resize')

class C:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return 'C(%r)' % (self.n,)

def
