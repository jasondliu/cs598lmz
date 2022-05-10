gi = (i for i in ())
# Test gi.gi_code.co_argcount = 0.
code = gi.gi_code
assert code.co_argcount == 0
assert code.co_varnames == ()
assert code.co_cellvars == ()
assert code.co_freevars == ()

gi = (i for i in () for j in ())
# Test gi.gi_code.co_argcount = 0.
code = gi.gi_code
assert code.co_argcount == 0
assert code.co_varnames == ()
assert code.co_cellvars == ()
assert code.co_freevars == ()

gi = (i for i in () for j in () for k in ())
# Test gi.gi_code.co_argcount = 0.
code = gi.gi_code
assert code.co_argcount == 0
assert code.co_varnames == ()
assert code.co_cellvars == ()
assert code.co_freevars == ()


def gen():
    yield 1

gi = gen()
code = gi.gi_code

