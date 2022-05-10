gi = (i for i in ())
# Test gi.gi_code.co_name.
assert gi.gi_code.co_name == ''
# Test gi.gi_frame.f_code.co_name.
assert gi.gi_frame.f_code.co_name == ''
# Test gi.gi_frame.f_lineno.
assert gi.gi_frame.f_lineno == 1

# Test the error messages.
try:
    gi.gi_frame.f_lasti = -1
except ValueError as e:
    assert str(e) == 'f_lasti must be >= 0'
try:
    gi.gi_frame.f_lasti = 100
except ValueError as e:
    assert str(e) == 'f_lasti must be < 100'

def f():
    yield

gi = (i for i in ())
# Test gi.next().
try:
    gi.next()
except StopIteration as e:
    assert str(e) == ''

gi = f()
# Test gi.next().
try:
    gi.
