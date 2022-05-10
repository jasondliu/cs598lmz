gi = (i for i in ())
# Test gi.gi_code.co_varnames
# XXX: This is a bit of a hack because we can't get the closure
# variables from the generator itself.
# Note that this is only true if the generator is being executed
# via a for loop.
gi = (i for i in (1,))
gi.gi_code.co_varnames
gi = (i for i in (1,2,3))
gi.gi_code.co_varnames
# Check that generators close over their locals 
def g():
    x = 1
    y = 2
    def inner():
        return x+y
    return inner
g()()
def g():
    x = 1
    y = 2
    gi = (x+y for i in ())
    return gi
g().gi_code.co_freevars
# Check that generators close over their locals (with defaults)
def g():
    x = 1
    y = 2
    gi = (x+y for i in () if True)
    return gi
g().gi_code.co_freevars
# Check that
