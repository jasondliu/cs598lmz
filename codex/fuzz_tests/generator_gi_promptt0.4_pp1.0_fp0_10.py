gi = (i for i in ())
# Test gi.gi_code.co_varnames
try:
    gi.gi_code.co_varnames
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_locals
try:
    gi.gi_frame.f_locals
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_back
try:
    gi.gi_frame.f_back
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_back.f_locals
try:
    gi.gi_frame.f_back.f_locals
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_back.f_back
try:
    gi.gi_frame.f_back.f_back
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi
