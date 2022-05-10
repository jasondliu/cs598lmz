gi = (i for i in ())
# Test gi.gi_code as it is not a direct attribute of PyGenObject
assert gi.gi_code is gi.__code__

inner1 = (i for j in (123,))
last_j = j
used_last_j = False
for i in inner1:
    used_last_j = True
assert not used_last_j

inner2 = (i for i, j in ((123, 456),))
# Test gi.gi_code as it is not a direct attribute of PyGenObject
assert inner2.gi_code is inner2.__code__
last_i = i
last_j = j
assert last_i == 123
assert last_j == 456

# This is to ensure that we save the cell correctly in the bytecode, as
# it's an interesting edge case for the transformation.
inner = (i for i, j in ((123, 456),))
assert inner.send(None) == 123

# And this one's to ensure that saving a cell at the beginning of the
# context is handled correctly (e.g. previously we weren't using
# the right
