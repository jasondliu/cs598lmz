gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == '<genexpr>'
assert not gi.gi_code.co_stacksize

# Test gi.gi_frame
assert gi.gi_frame.f_code.co_name == '<genexpr>'

# Test gi.gi_running
assert not gi.gi_running

def g():
    pass

# Test g.__code__
assert g.__code__.co_name == 'g'
assert g.__code__.co_stacksize
assert g.__code__.co_varnames == ('',)

# Test g.__defaults__
assert not g.__defaults__

# Test g.__globals__
assert g.__globals__['g'] is g

# Test g.__closure__
assert not g.__closure__

# Test g.__dict__
assert g.__dict__ == type(g).__dict__

# Test g.__doc__
assert g.__doc__ is None

# Test
