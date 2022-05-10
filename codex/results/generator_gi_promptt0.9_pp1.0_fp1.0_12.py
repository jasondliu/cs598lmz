gi = (i for i in ())
# Test gi.gi_code is None when no code is defined
gi = (i for i in ())
# Test gi.gi_frame is None when no code is defined
gi = (i for i in ())
# Test gi.gi_running is False when no code is defined
gi = (i for i in ())
# Test gi.gi_yieldfrom is None when no code is defined
gi = (i for i in ())
# Issue #20532: Check for AttributeErrors, not AttributeError:
# Test gi.gi_frame is not None when code is defined
gi = (i for i in ())
# Test gi.gi_frame.f_lasti is not None when code is defined
gi = (i for i in ())
# Test gi.gi_frame.f_code is not None when code is defined
gi = (i for i in ())
# Test gi.gi_frame.f_back is None when code is defined
gi = (i for i in ())
# Test gi.gi_frame.f_locals is not None when code is defined
gi = (i for i in ())

