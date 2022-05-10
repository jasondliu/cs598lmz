gi = (i for i in ())
# Test gi.gi_code syntax error
try:
    gi.gi_code = gi
    assert False
except AttributeError:
    pass
# Test gi.gi_frame syntax error
try:
    gi.gi_frame = gi
    assert False
except AttributeError:
    pass
# Test gi.gi_running syntax error
try:
    gi.gi_running = gi
    assert False
except AttributeError:
    pass
# Test gi.gi_yieldfrom syntax error
try:
    gi.gi_yieldfrom = gi
    assert False
except AttributeError:
    pass
