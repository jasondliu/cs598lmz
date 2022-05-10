gi = (i for i in ())
# Test gi.gi_code.co_flags is changed
assert next(gi).gi_code.co_flags & 4 == 0
assert next(gi).gi_code.co_flags & 4 != 0
# XXX
gi = (i for i in ())
assert next(gi).gi_code.co_flags & 4 == 0
assert next(gi).gi_code.co_flags & 4 != 0
#
# Should have set frame.f_back (each call adds a frame)
#
try:
    gi.throw(AssertionError)
except AssertionError:
    assert sys.exc_info()[2].tb_frame.f_back is not None
else:
    assert False, 'No exception thrown'

try:
    gi.throw(AssertionError)
except AssertionError:
    assert sys.exc_info()[2].tb_frame.f_back is not None
else:
    assert False, 'No exception thrown'

try:
    gi.throw(AssertionError)
except AssertionError:
    assert sys.exc_info
