import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect:

class A:

    def __init__(self):
        self.indirect = None

    def __del__(self):
        pass

a = A()
a.indirect = a
a.__class__.__bases__
# The 'gc' module's test harness uses a weak ref to gc_collect(), to make
# sure that gc_collect() doesn't collect itself (issue #17004):

class TestHarness:

    def __init__(self):
        self.c = [gc_collect]
        self.wr = weakref.ref(self.c)

    def run(self):
        self.c = None
        gc.collect()
        if self.wr() is None:
            raise "failed"

t = TestHarness()
t.run()
# Verify that garbage that's already been collected is ignored

class A:

    def __init__(self):
        self.indirect = None

    def __del__(self):
        pass

a = A()
a.indirect = a
wr = weak
