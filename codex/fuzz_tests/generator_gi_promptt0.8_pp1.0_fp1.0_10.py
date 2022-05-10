gi = (i for i in ())
# Test gi.gi_code is None
trace(gi)

# Make sure the iterator doesn't get freed prematurely
for i in range(100):
    tuple(gi)

# Verify that code is actually freed
import gc
gc.collect()

# Import again to make sure it can return correctly
# even though the first import has been freed
import gi

# Test gi_code is not None
gi = (i for i in (1,))
trace(gi)
