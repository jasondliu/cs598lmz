gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_code.co_flags
gi.gi_code.co_flags
