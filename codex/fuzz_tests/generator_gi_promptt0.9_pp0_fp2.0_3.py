gi = (i for i in ())
# Test gi.gi_code is <code object <genexpr>
# And test that gi.gi_frame is not NULL
# This unit test doesn't work with work-alike generators
assert(isinstance(gi.gi_code, types.CodeType))
assert(gi.gi_frame is not None)
