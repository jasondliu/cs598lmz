gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_name
try:
    gi.gi_name
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_qualname
try:
    gi.gi_qualname
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_code.co_name)
print(gi.gi_frame)
print
