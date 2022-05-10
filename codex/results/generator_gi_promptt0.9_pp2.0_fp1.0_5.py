gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<locals>'
try:
  next(gi)
except StopIteration:
  err = sys.exc_info()[1]
else:
  assert False
# Check err
assert err.value == test_value
