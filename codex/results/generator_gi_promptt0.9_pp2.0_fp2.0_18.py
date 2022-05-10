gi = (i for i in ())
# Test gi.gi_code.co_varnames.  repr() of an empty tuple
# returns an empty string.
assert eval(repr(gi)).gi_code.co_varnames == ()

# Test gi.gi_code.co_varnames.  repr() of a non-empty tuple
# returns a string starting with "(", e.g. "(a, b)".
gi = (i for i in range(1))
assert eval(repr(gi)).gi_code.co_varnames == ('.0',)

# Test gi.gi_frame.f_locals.  repr() of an empty dict
# returns an empty string.
gi = (i for i in () for i in ())
assert eval(repr(gi)).gi_frame.f_locals == {}

# Test gi.gi_frame.f_locals.  repr() of a non-empty dict
# returns a string starting with "{", e.g. "{'a': 3}".
gi = (i for i in (i for i in ()))
assert eval(repr(gi)).gi_
