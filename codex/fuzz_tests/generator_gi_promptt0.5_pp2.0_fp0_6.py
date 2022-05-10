gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_code.co_filename
assert gi.gi_code.co_filename == '<stdin>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == '<stdin>'

# Test gi.gi_code.co_name, co_filename
def f():
    return (i for i in ())
gi = f()
assert gi.gi_code.co_name == 'f'
assert gi.gi_code.co_filename == __file__
assert gi.gi_frame.f_code.co_name == 'f'
assert gi.gi_frame.f_code.co_filename == __file__

# Test gi.gi_code.co_
