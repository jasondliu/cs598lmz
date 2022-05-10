gi = (i for i in ())
# Test gi.gi_code == NULL
g = gi.gi_code
assert isinstance(g, types.CodeType)
assert g is None

# Test gi.gi_frame == NULL
g = gi.gi_frame
assert isinstance(g, types.FrameType)
assert g is None

# Test gi.gi_running == 0
g = gi.gi_running
assert g == 0

# Test gi.gi_yieldfrom == NULL
g = gi.gi_yieldfrom
assert isinstance(g, types.FrameType)
assert g is None

# Test gi.gi_weakreflist == NULL
g = gi.gi_weakreflist
assert isinstance(g, list)
assert len(g) == 0

# Test gi.gi_finalizer == NULL
g = gi.gi_finalizer
assert g is None

l = [0, 1, 2, 3, 4]

I = iter(l)

# Test I.__class__.__name__ == 'list_iterator'
assert isinstance(I,
