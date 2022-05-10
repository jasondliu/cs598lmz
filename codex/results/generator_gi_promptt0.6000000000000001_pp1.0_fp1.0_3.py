gi = (i for i in ())
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()
# Test gi.gi_code.co_argcount
assert gi.gi_code.co_argcount == 0

gi = (i for i in (1, 2, 3))
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()
# Test gi.gi_code.co_argcount
assert gi.gi_code.co_argcount == 0

gi = (i for i in (1, 2, 3) if i)
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ('i',)
# Test gi.gi_code.co_argcount
assert gi.gi_code.co_argcount == 0

def f():
    return (i for i in (1, 2, 3) if i)

gi = f()
# Test gi.gi_code.co_varnames
assert
