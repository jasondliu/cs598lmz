gi = (i for i in ())
# Test gi.gi_code
i, = (i for i in ())
# Test gi.gi_name
i, = (i for i in ())
# Test gi.gi_yieldfrom
i, = (i for i in ())

# Test for the presence of gi_running with the presence of GEN_RUNNING and
# gi_yieldfrom.
# See http://bugs.python.org/issue28790.
# Test gi.gi_running
i, = (i for i in ())

# Test that the generator gi.gi_frame.f_lasti doesn't points to BB_SETUP_GENERATOR:
GeneratorExit

# Test gf.f_code, f_nlocals, f_stacksize and f_stackedlocals
# Test gf.f_code == function.__code__
# Test gf.f_stack and gf.f_lasti
i, = (i for i in ())

# Test that gf.f_valuestack matches gf.f_stack.
i, = (i for i in ())
#
