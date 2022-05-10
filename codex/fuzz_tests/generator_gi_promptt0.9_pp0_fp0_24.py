gi = (i for i in ())
# Test gi.gi_code is not NULL
try:
    gi.gi_code
except AttributeError:
    pass
else:
    raise TestFai
