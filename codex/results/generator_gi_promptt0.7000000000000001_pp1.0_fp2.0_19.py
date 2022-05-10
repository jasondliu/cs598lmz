gi = (i for i in ())
# Test gi.gi_code.co_name.
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_lasti
try:
    gi.send(10)
except TypeError:
    assert gi.gi_frame.f_lasti == -1
