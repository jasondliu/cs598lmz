gi = (i for i in ())
# Test gi.gi_code.co_code is set to NULL.
try:
    gi.gi_code.co_code
except ValueError:
    pass
else:
    print("FAILED: gi.gi_code.co_code is not set to NULL")

# Test gi.gi_code.co_consts is set to NULL.
try:
    gi.gi_code.co_consts
except ValueError:
    pass
else:
    print("FAILED: gi.gi_code.co_consts is not set to NULL")

# Test gi.gi_code.co_names is set to NULL.
try:
    gi.gi_code.co_names
except ValueError:
    pass
else:
    print("FAILED: gi.gi_code.co_names is not set to NULL")

# Test gi.gi_code.co_varnames is set to NULL.
try:
    gi.gi_code.co_varnames
except ValueError:
    pass
else:
    print("FAIL
