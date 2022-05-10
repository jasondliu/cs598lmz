gi = (i for i in ())
# Test gi.gi_code.co_zombieframe
#
# The test is a bit artificial, because we need to create a generator
# object, and then kill its frame, so that the generator can't actually
# be used in a for loop.  But it does test the zombie-frame machinery.

import _testcapi

gi = _testcapi.make_generator_with_zombie_frame()

# Check that the frame is marked as zombie
assert gi.gi_frame.f_lasti == -1

# Check that the generator can be finalized
import gc
gc.collect()

# Check that the frame is still marked as zombie
assert gi.gi_frame.f_lasti == -1
