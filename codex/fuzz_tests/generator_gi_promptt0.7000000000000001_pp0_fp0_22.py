gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("SKIP")
    raise SystemExit

gi = (i for i in ())
next(gi)
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("SKIP")
    raise SystemExit


def gen():
    yield


gi = gen()
# Test gi.gi_frame.f_lasti
try:
    gi.gi_frame.f_lasti
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_code
try:
    gi.gi_frame.f_code
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

