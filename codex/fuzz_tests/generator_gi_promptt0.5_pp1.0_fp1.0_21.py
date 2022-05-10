gi = (i for i in ())
# Test gi.gi_code.co_name
try:
    gi.gi_code.co_name
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_code.co_filename
try:
    gi.gi_code.co_filename
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_back
try:
    gi.gi_frame.f_back
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_back.f_back
try:
    gi.gi_frame.f_back.f_back
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_lineno
try:
    gi.gi_frame.f_lineno
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_lasti
try:
   
