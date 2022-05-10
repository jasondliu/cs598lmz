gi = (i for i in ())
# Test gi.gi_code (gi_code.c, gi_code.h, refcounts.inc)
gi.gi_code
gi.gi_code.co_argcount
gi.gi_code.co_code
gi.gi_code.co_consts
gi.gi_code.co_filename
gi.gi_code.co_firstlineno
gi.gi_code.co_flags
gi.gi_code.co_lnotab
gi.gi_code.co_name
gi.gi_code.co_names
gi.gi_code.co_nlocals
gi.gi_code.co_stacksize
gi.gi_code.co_varnames   # Dropped support in 4.0

# Note: since this procedure is buggy, we cannot safely test any more
# attributes of gi (i.e. we might crash Python)


try:
    gi.gi_frame
except ValueError:
    pass
else:
    raise TestFailed("ValueError not raised")

# Test frame suspension (frameobject.c, frameobject.h, object.c
