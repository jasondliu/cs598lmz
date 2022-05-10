import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() returns a non-zero list on collectable objects
class Foo:
    pass
gc.collect()
foo = Foo()
f = weakref.ref(foo)
gc.collect()

class GCTrigger(object):
    def __init__(self):
        # Create self-cycles
        self.subob = self

    def __del__(self):
        gc.collect()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return


trigger = GCTrigger()

# Ensure the return value of gc.collect() is non-zero
with trigger:
    gc.collect()
