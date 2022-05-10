gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'

# Test gi.gi_code.co_name
def f():
    yield 1

gi = f()
assert gi.gi_code.co_name == 'f'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'f'

# Test gi.gi_code.co_name
def f():
    yield from (i for i in ())

gi = f()
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'f'

# Test gi.gi_code.co_name
def f():
    yield from
