import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

foo = Foo()
foo.attr = Foo()
foo.attr.attr = Foo()
foo.attr.attr.attr = foo
del foo

# Now collect anything which can be collected.
print(gc.collect())
# 0 objects in 0 generations.
print(gc.garbage)
# []

# Collect garbage which is uncollectable, and unreachable.
print(gc.collect(2))
# 0 objects in 0 generations.
print(gc.garbage)
# []


# Make an object which is collectable, but has a cycle to it.

class Bar:
    pass

bar = Bar()
bar.attr = Bar()
bar.attr.attr = Bar()
bar.attr.attr.attr = bar

# Collect garbage which is collectable, but has a cycle to it.
print(gc.collect())
# 3 objects in 1 generations.
print(gc.garbage)
# [<__main__.Bar instance at 0x7ffc3b44>]

# Collect garbage which is collectable, but has a
