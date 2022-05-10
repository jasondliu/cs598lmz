gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_name
gi.gi_name
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test types.CodeType
def f(): pass
# Test the existence of code.co_code
f.__code__.co_code
# Test the existence of code.co_consts
f.__code__.co_consts
# Test the existence of code.co_names
f.__code__.co_names
# Test the existence of code.co_varnames
f.__code__.co_varnames
# Test the existence of code.co_freevars
f.__code__.co_freevars
# Test the existence of code.co_cellvars
f.__code__.co_cellvars
# Test the existence of code.co_filename
f.__code__.co_filename
# Test the existence of code.co_name
