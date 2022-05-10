gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

def f():
    yield 1

gf = f()
# Test gf.gi_code
try:
    gf.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_frame
try:
    gi.gi_frame
except ValueError:
    print('SKIP')
    raise SystemExit

# Test gf.gi_frame
try:
    gf.gi_frame
except ValueError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_running
try:
    gi.gi_running
except ValueError:
    print('SKIP')
    raise SystemExit

# Test gf.gi_running
try:
    gf.gi_running
except ValueError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_yieldfrom
try:
    gi.
