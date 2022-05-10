import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations() with a list
class TestObject(object):
    def __del__(self):
        # Induce a small cycle
        self.referrer = self
        gc.collect_generations()
        # Ensure that we are out of reach
        assert self.referrer.referrer is not self

# no collecting
o = TestObject()
referrers = gc.get_referrers(o)
refs = referrers[0]
# hackish: XXX what is a better way to determine if something is a dict?
d = dict([[o, o]])
assert dict is type(d)
assert id(o) in d
# could check for d.has_key(o) and d[o] is o
assert len(list(d.items())) == 1

# collecting the list
o = TestObject()
list([o, o])
gc.collect_generations()

# collect everything
class A:
    pass

# no collecting
o = TestObject()
a = A()
a.attr = o
referrers
