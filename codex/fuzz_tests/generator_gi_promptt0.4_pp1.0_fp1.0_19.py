gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == ''
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == ''

# Test generator expression
gi = (i for i in range(10))
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == ''
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == ''

# Test generator function
def gen_fn():
    yield 1

gi = gen_fn()
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == 'gen_fn'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'gen_fn'

# Test generator function with default argument
def gen_fn_default(a=1):
    yield a

gi
