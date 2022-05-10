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

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print('SKIP')
    raise SystemExit


def gen():
    yield

gi = gen()
next(gi)

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print('SKIP')
    raise SystemExit


def gen():
    yield from range(3)

gi = gen()
next(gi)

# Test gi.gi_frame
try:
    gi.gi
