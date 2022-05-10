gi = (i for i in ())
# Test gi.gi_code == gi.__code__
CodeType = type(gi.gi_code)
assert type(gi.__code__) == CodeType
assert gi.gi_code == gi.__code__
