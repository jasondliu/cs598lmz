gi = (i for i in ())
# Test gi.gi_code.co_filename
# Bug #102322
gi.gi_code.co_filename

# Test gi.gi_frame.f_code.co_filename
# Bug #102322
gi.gi_frame.f_code.co_filename

# Test gi.gi_frame.f_locals.items()
# Bug #102322
gi.gi_frame.f_locals.items()

# Test gi.gi_frame.f_locals.keys()
# Bug #102322
gi.gi_frame.f_locals.keys()

# Test gi.gi_frame.f_locals.values()
# Bug #102322
gi.gi_frame.f_locals.values()

# Test gi.gi_frame.f_globals.items()
# Bug #102322
gi.gi_frame.f_globals.items()

# Test gi.gi_frame.f_globals.keys()
# Bug #102322
gi.gi_frame.f_glob
