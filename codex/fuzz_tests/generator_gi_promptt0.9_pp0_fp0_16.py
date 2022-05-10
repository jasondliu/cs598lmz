gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_code.co_argcount == 0
gi = (i for i in ())
# Test gi.__code__
assert gi.__code__.co_name == '<genexpr>'
assert gi.__code__.co_argcount == 0
