gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'

# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'test_generator_expression'

# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 5

# Test gi.gi_frame.f_trace
assert gi.gi_frame.f_trace is None

# Test gi.gi_running
assert gi.gi_running is False

# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None

# Test gi.send
assert gi.send(None) == 0

# Test gi.throw
try:
    gi.throw(ValueError)
except ValueError:
    pass
else:
    assert False

