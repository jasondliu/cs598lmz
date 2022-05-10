gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 3

it = [1, 2, 3].__iter__()
# Test it.im_self
assert it.im_self == [1, 2, 3]

ci = (i for i in range(0)).__iter__()
# Test ci.gi_code.co_name
assert ci.gi_code.co_name == '<genexpr>'

gi = (i for i in ())
# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 3

it = [1, 2, 3].__iter__()
# Test it.im_func
assert it.__func__ == it.__class__.__iter__

ci = (i for i in range(0)).__iter__()
# Test ci.gi_frame.f_code.co_firstlineno
assert ci.gi_frame.f_code.co_firstlineno == 3

gi = (i for i in ())

