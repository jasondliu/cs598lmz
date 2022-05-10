gi = (i for i in ())
# Test gi.gi_code.co_varnames
assert gi.gi_code.co_varnames == ()

# Test function().gi_code.co_varnames
def f1(): return
assert f1.gi_code.co_varnames == ()

# Define a function that takes a param
def f2(arg): return
assert f2.gi_code.co_varnames == ('arg',)

# Define a nested function and make sure the co_varnames is correct
def f3():
    def g(): return
    assert g.gi_code.co_varnames == ()
    return 1
f3()

# Test co_varnames attribute
def f4(a):
    def g(b): return 1, b

    x = 2
    y = 3
    if a:
        h = g(x)
    else:
        h = g(y)

    z = 4, 5
    return h, z

assert f4(False)[0][0] == 1 and f4(False)[1] == (4, 5)
