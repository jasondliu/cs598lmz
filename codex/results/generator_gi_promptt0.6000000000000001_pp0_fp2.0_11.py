gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code
gi.gi_frame
gi.gi_running
gi.gi_yieldfrom
gi.gi_name
gi.gi_frame.f_lasti

# Test gi.gi_code is not None
gi = (i for i in range(10))
gi.gi_code
gi.gi_frame
gi.gi_running
gi.gi_yieldfrom
gi.gi_name
gi.gi_frame.f_lasti

# Test gi_running is 1
gi.gi_running
gi.gi_frame.f_lasti

# Test gi_running is 0
next(gi)
gi.gi_running
gi.gi_frame.f_lasti

# Test StopIteration
next(gi)
gi.gi_running
gi.gi_frame.f_lasti

# Test StopIteration
next(gi)
gi.gi_running
gi.gi_frame.f_lasti

# Test StopIteration
next(gi)
gi.gi_running
gi.gi_frame.
