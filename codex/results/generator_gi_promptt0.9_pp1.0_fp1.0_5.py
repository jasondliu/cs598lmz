gi = (i for i in ())
# Test gi.gi_code is still a function
try:
    gi.gi_code.co_code
except AttributeError:
    print("SKIP")
    raise SystemExit

print("method")
