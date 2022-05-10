gi = (i for i in ())
# Test gi.gi_code to make sure it is not NULL
gi.gi_code

# Test that gi.gi_frame is NULL
gi.gi_frame is None

# Test gi.gi_running to make sure it is false
gi.gi_running is False

# Test gi.gi_yieldfrom to make sure it is NULL
gi.gi_yieldfrom is None

# Test gi.gi_name to make sure it is NULL
gi.gi_name is None

# Test gi.gi_qualname to make sure it is NULL
gi.gi_qualname is None

# Test gi.gi_weakreflist to make sure it is NULL
gi.gi_weakreflist is None

# Test gi.gi_exc_state to make sure it is NULL
gi.gi_exc_state is None

# Test gi.gi_exc_traceback to make sure it is NULL
gi.gi_exc_traceback is None

# Test gi.gi_exc_type to make sure it is NULL
gi.gi_exc_type is None

#
