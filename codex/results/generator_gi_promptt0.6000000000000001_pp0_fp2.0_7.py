gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")
# Test gi.gi_frame is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print("AttributeError expected")
# Test gi.gi_running is False
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print("AttributeError expected")
# Test gi.gi_yieldfrom is None
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print("AttributeError expected")


# Test a generator that has yielded.
def gen():
    yield 1
gi = gen()
# Test gi.gi_code is not None
if gi.gi_code is not None:
    pass
else:
    print("gi.gi_code is None")
# Test gi.gi_frame is not None
if gi.gi_frame is not None:
    pass
