import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect not only collect objects in unreachable cycles, but also
# call tp_clear on those objects.
class C:
    def __init__(self):
        self.a = 1
    def __del__(self):
        if hasattr(self, 'a'):
            raise RuntimeError("tp_clear not called")

# Make sure the instance dict is large enough to be split.
for i in range(256):
    globals()['k%d'%i] = i

def make_cycle():
    c = C()
    c.b = c
    return c

# Create a bunch of cyclic trash.
for i in range(20):
    make_cycle()
gc.collect()

# Check that the cyclic trash objects have been cleared.
if gc.garbage:
    print(gc.garbage)
    raise RuntimeError("uncollectable garbage not cleared")

# Create a bunch of cyclic trash.
for i in range(20):
    make_cycle()
    gc.collect()

# Check that the cyclic trash objects have been
