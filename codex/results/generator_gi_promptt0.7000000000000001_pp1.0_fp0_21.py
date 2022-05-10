gi = (i for i in ())
# Test gi.gi_code.co_varnames
gi.gi_code.co_varnames
# Test gi.gi_code.co_argcount
gi.gi_code.co_argcount

def f():
    return (i for i in ())

# Test f().gi_code.co_varnames
f().gi_code.co_varnames
# Test f().gi_code.co_argcount
f().gi_code.co_argcount

# Tuple should be returned unmodified.
t = (1, 2, 3)
# Test t.gi_code
t.gi_code
# Test t.gi_frame
t.gi_frame
# Test t.gi_running
t.gi_running
# Test t.gi_yieldfrom
t.gi_yieldfrom
