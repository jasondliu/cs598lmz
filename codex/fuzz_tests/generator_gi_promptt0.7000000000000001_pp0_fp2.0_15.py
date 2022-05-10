gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame
if gi.gi_frame is not None:
    print("SKIP")
    raise SystemExit

# Test gi.gi_running
if gi.gi_running:
    print("SKIP")
    raise SystemExit

# Test gi.gi_yieldfrom
if gi.gi_yieldfrom is not None:
    print("SKIP")
    raise SystemExit
