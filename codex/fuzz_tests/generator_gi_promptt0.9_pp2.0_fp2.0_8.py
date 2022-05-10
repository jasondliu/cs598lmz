gi = (i for i in ())
# Test gi.gi_code
'function code' in dir(gi.gi_code)

# Test gi.gi_frame
'f_globals' in dir(gi.gi_frame)

# Test gi.gi_running
'func_name' in dir(gi.gi_running)
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running is None
gi.gi_running.__name__
'generator'

# Test gi.gi_yieldfrom
'__name__' in dir(gi.gi_yieldfrom)
gi.gi_yieldfrom.__name__
'generator'

# Test sys.stdin
'device' in dir(sys.stdin)

# Test sys.stdout
'device' in dir(sys.std
