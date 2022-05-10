import weakref
# Test weakref.ref copy and deepcopy.
# The keys in expected_identical are the ids of weakrefs and
# their value is the id of their referent, or 0 if it is None.
# Both keys and values are lists, one entry for each round.
# The values 0, 1, etc are actually the ids of the integers
# 0, 1, etc and 0 means None.  By using integers as referents
# we can be sure of their identity.
#
# These dictionaries are compared before and after the test.
# This allows the test code to add a round before and after the
# test functions, so we can be sure that all weakrefs have been
# cleared.

import weakref
ref = weakref.ref
ref_nothing = ref(None)
ref_zero = ref(0)
ref_one = ref(1)
expected_identical = {ref_nothing: [0], ref_zero: [1], ref_one: [2]}

def copy_test():
    wrs = [ref_nothing, ref_zero, ref_one]
    w1 = wrs +
