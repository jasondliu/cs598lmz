import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs. This test takes about 0.4 seconds on a
# 300MHz Pentium II.  It does two passes over all the objects, and checks
# that everything gets cleared during the second pass.  If not, the
# commented out print statements can be uncommented to see what's left
# behind.  This assumesPython releases the objects out of the list in order
# (which seems to be the case) and that the list gc.garbage is reordered to
# place collectable objects earlier in the list.  This could be fixed by
# sorting the list before making this comparison.

# TODO: Introduce more cases where an object has a __del__() method.  Some
# cases to try:
#
#   - foo.__del__() uses feep()
#   - bar.__del__() modifies foo
#   - baz.__del__() modifies bar
#   - baz.__del__() uses feep()

# TODO: This reuses a lot of code from test_weakref.  It would be nice to
# be able to share the code somehow
