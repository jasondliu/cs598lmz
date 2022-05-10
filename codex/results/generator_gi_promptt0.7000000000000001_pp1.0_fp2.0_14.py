gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == CO_GENERATOR, gi.gi_code.co_flags
# Test gi.gi_frame
assert gi.gi_frame.f_code is gi.gi_code, gi.gi_frame.f_code

# Bug 933: Make sure that a generator's gi_frame.f_exc_type member is
# set to None when the generator is not in an exception state.

def foo():
    yield 1
g = foo()
assert g.gi_frame.f_exc_type is None, g.gi_frame.f_exc_type
try:
    raise RuntimeError
except RuntimeError:
    g.throw(RuntimeError)
assert g.gi_frame.f_exc_type is RuntimeError, g.gi_frame.f_exc_type

# Test gi_frame.f_lasti

def foo():
    yield 1
g = foo()
assert g.gi_frame.f_lasti == -1, g.gi_frame.f_last
