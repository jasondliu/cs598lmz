gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
    raise TestFailed('gi_code is not read-only')
except AttributeError:
    pass
# Test gi.gi_frame
try:
    gi.gi_frame
    raise TestFailed('gi_frame is not read-only')
except AttributeError:
    pass
# Test gi.gi_running
try:
    gi.gi_running
    raise TestFailed('gi_running is not read-only')
except AttributeError:
    pass
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
    raise TestFailed('gi_yieldfrom is not read-only')
except AttributeError:
    pass
try:
    gi.gi_name
    raise TestFailed('gi_name is not read-only')
except AttributeError:
    pass
gi.gi_name = 'foo'

# Test that generator expressions return the correct type
def g():
    yield from (x for x in (1, 2, 3))

