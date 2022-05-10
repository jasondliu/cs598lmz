gi = (i for i in ())
# Test gi.gi_code.co_name is bound to the class method name.
assert gi.gi_code.co_name == 'gi'

# Test that gi.gi_code.co_filename is bound to the class method filename.
assert gi.gi_code.co_filename == '<stdin>'

# Test that gi.gi_code.co_firstlineno is bound to the class method line number.
assert gi.gi_code.co_firstlineno == 13

# Test that gi.gi_code.co_argcount is bound to the number of arguments.
assert gi.gi_code.co_argcount == 0

# Test that gi.gi_code.co_varnames is bound to the argument names.
assert gi.gi_code.co_varnames == ()

# Test that gi.gi_code.co_flags is bound to the method flags.
assert gi.gi_code.co_flags == 67

# Test that gi.gi_frame.f_locals is bound to the method locals.
gf = g
