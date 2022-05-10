gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame are set
# Note that the code object is not the same as __code__, which is the
# code object of the next outer frame.  gi is its own frame, thus it
# has its own code object.
assert gi.gi_code is gi.gi_frame.f_code
assert gi.gi_frame.f_code is gi.gi_frame.f_code
assert gi.gi_frame.f_code is gi.__code__
assert gi.gi_frame.f_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_freevars == ()
assert gi.gi_frame.f_code.co_firstlineno == 1
assert gi.gi_frame.f_code.co_lnotab is not None

# Test gi_frame.f_lasti
def se():
    yield 1
    yield 2
    yield 3
gi = se()
assert gi.gi_frame.f_lasti == -1
# next()
