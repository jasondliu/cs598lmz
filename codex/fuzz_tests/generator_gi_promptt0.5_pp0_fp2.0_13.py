gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

code = gi.gi_code

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("SKIP")
    raise SystemExit

frame = gi.gi_frame

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print("SKIP")
    raise SystemExit

running = gi.gi_running

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print("SKIP")
    raise SystemExit

yieldfrom = gi.gi_yieldfrom
