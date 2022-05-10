import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for i in range(2):
    gc.collect()
# Test gc.garbage
gc.garbage[:] = [42, 'spam', 1, 1.1, [2, 3], 'spam']
gc.collect()
print(gc.garbage)
# Test gc.get_count()
print(gc.get_count())
# Test gc.get_debug()
print(gc.get_debug())
# Test gc.get_threshold()
print(gc.get_threshold())
# Test gc.get_referrers(object)
class Foo:
    pass
foo = Foo()
print(gc.get_referrers(foo))
# Test gc.get_referents(object)
class Bar:
    pass
bar = Bar()
print(gc.get_referents(bar))
# Test gc.is_tracked(object)
print(gc.is_tracked(bar))
# Test gc.is_finalized(object)
print(gc.is_finalized(bar))

