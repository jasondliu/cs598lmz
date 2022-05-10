import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()


gc.garbage

def f():
    return {}

def g():
    return gc.garbage[0]

def h():
    return weakref.ref(gc.garbage[0])

class C:
    def __del__(self):
        print 'del C'

def test(d, c=C()):
    d[0] = c
    d[1] = d
    del c

test(f())
test(g())
test(h())

# Print the garbage cycle
gc.collect()
len(gc.garbage)
