gi = (i for i in ())
# Test gi.gi_code
# gi.gi_code = None
# Test gi.gi_frame
# gi.gi_frame = None
# Test gi.gi_running
# gi.gi_running = None
# Test gi.gi_yieldfrom
# gi.gi_yieldfrom = None
# Test gi.gi_weakreflist
# gi.gi_weakreflist = None
# Test gi.gi_name
# gi.gi_name = None
# Test gi.gi_qualname
# gi.gi_qualname = None
# Test gi.gi_frame
# gi.gi_frame = None

# Test generator.gi_running
gi = (i for i in ())
gi.gi_running = None

# Test generator.gi_code
gi = (i for i in ())
gi.gi_code = None

# Test generator.gi_frame
gi = (i for i in ())
gi.gi_frame = None

# Test generator.gi_yieldfrom
gi = (i for i in ())
gi
