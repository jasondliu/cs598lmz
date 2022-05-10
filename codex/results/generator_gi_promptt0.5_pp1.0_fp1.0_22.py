gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_running
# Test gi.gi_yieldfrom
try:
    gi.gi_running
    gi.gi_yieldfrom
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.__name__
# Test gi.__qualname__
try:
    gi.__name__
    gi.__qualname__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.__next__
try:
    gi.__next__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.send
# Test gi.throw
# Test gi.close
try:
    gi.
