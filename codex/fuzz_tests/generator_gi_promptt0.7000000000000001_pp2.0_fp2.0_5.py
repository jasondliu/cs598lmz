gi = (i for i in ())
# Test gi.gi_code.co_filename
assert next(gi).co_filename == "<genexpr>"

# Test gi.gi_code.co_firstlineno
assert next(gi).co_firstlineno == 1

# Test gi.gi_code.co_name
assert next(gi).co_name == "<genexpr>"

# Test gi.gi_code.co_varnames
assert next(gi).co_varnames == ("i",)

# Test gi.gi_frame
assert next(gi).gi_frame is None

# Test gi.gi_running
assert next(gi).gi_running == 0

# Test gi.gi_yieldfrom
assert next(gi).gi_yieldfrom is None

gi = (i for i in ())
try:
    next(gi)
except StopIteration as e:
    # Test gi.gi_exception
    assert gi.gi_exception is e

gi = (i for i in ())
# Test gi.gi_frame.f_lasti
try:
    next(
