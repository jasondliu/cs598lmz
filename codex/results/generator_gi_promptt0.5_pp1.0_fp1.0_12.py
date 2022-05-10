gi = (i for i in ())
# Test gi.gi_code
assert type(gi.gi_code) is types.CodeType
assert gi.gi_code.co_argcount == 1
assert gi.gi_code.co_varnames == ("i",)
assert gi.gi_code.co_name == "i"
# Test gi.gi_frame
assert type(gi.gi_frame) is types.FrameType
# Test gi.gi_running
assert type(gi.gi_running) is types.TracebackType
# Test gi.gi_frame.f_locals
assert gi.gi_frame.f_locals == {}
# Test gi.gi_frame.f_globals
assert gi.gi_frame.f_globals == globals()

# Test generator.gi_throw()
def throw_gen():
    yield 1
    yield 2
    yield 3

g = throw_gen()
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

try:
    g.gi_throw(ValueError)
except Value
