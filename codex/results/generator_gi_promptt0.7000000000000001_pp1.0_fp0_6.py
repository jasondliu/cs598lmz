gi = (i for i in ())
# Test gi.gi_code gives None in the case of a generator iterator.
assert gi.gi_code is None
assert gi.gi_frame.f_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_firstlineno == 2

# The following code is invalid, because gi_code is not available.
#try:
#    gi.gi_code.co_name
#except AttributeError:
#    print("AttributeError")

def f(x):
    return (i for i in (x,))

g = f(5)
assert g.gi_code.co_name == 'f'
assert g.gi_frame.f_code.co_name == '<genexpr>'

# The following code is invalid, because gi_code is not available.
#try:
#    g.gi_code.co_name
#except AttributeError:
#    print("AttributeError")
