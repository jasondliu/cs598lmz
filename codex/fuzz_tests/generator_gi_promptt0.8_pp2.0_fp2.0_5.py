gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code is None
# Test next(gi) raises StopIteration
with raises(StopIteration):
    next(gi)
# Test gi.gi_code is None
gi.gi_code is None
# Test gi.gi_frame is None
gi.gi_frame is None
# Test gi.gi_running is False
gi.gi_running is False
# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom is None

# Test gi = (i**2 for i in range(10))
gi = (i**2 for i in range(10))
# Test next(gi) is 0
next(gi) is 0
# Test gi.gi_frame.f_lasti == -1
gi.gi_frame.f_lasti == -1
# Test gi.gi_code.co_firstlineno == 1
gi.gi_code.co_firstlineno == 1
# Test gi.gi_frame.f_code.co_firstlineno == 1
gi.gi_frame.f_
