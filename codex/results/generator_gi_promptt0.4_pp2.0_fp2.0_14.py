gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags & CO_GENERATOR == CO_GENERATOR

assert (i for i in ()).gi_code.co_flags & CO_GENERATOR == CO_GENERATOR

# Test gi_frame.f_lasti
def f():
    yield 1

gi = f()
assert gi.gi_frame.f_lasti == -1

gi.next()
assert gi.gi_frame.f_lasti == 0

# Test gi_frame.f_code.co_flags
assert gi.gi_frame.f_code.co_flags & CO_GENERATOR == CO_GENERATOR

# Test gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'f'

# Test gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == __file__

# Test gi_frame.f_code.co_firstlineno
