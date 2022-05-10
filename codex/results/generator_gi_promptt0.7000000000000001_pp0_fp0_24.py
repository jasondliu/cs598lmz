gi = (i for i in ())
# Test gi.gi_code.co_name
gi = iter(callable, None)
gi = (i for i in ())
# Test gi.gi_code.co_name

# gi_frame
gi = iter(())
# Test gi.gi_frame.f_code.co_name
gi = iter(callable, None)
# Test gi.gi_frame.f_code.co_name

# gi_running
gi = iter(())
# Test gi.gi_running
gi = iter(callable, None)
# Test gi.gi_running

# gi_yieldfrom
# Test gi.gi_yieldfrom
gi = iter(())
# Test gi.gi_yieldfrom
gi = iter(callable, None)
# Test gi.gi_yieldfrom
gi = (i for i in ())
# Test gi.gi_yieldfrom
gi = (i for i in ())
# Test gi.gi_yieldfrom
gi = (i async for i in ())
# Test gi.gi_yieldfrom
gi
