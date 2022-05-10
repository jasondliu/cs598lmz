gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_running is False
try:
    gi.gi_running
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom = -1
print(gi.gi_yieldfrom)
gi.gi_yieldfrom = None
print(gi.gi_yieldfrom)

# Test gi.gi_frame.f_lasti is None
gi.gi_frame = inspect.currentframe()
try:
    gi.gi_frame.f_lasti
except AttributeError:
    print('SKIP')
    raise SystemExit
