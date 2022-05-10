gi = (i for i in ())
# Test gi.gi_code.co_code directly.
for i in gi:
    pass
TestError(TypeError, globals, ())
del i  # clear any reference to the iterator object
gi = None
gi2 = (i for i in ())
gi3 = (i for i in ())
gi4 = (i for i in ())
gi5 = (i for i in ())
gi6 = (i for i in ())
gi7 = (i for i in ())
for i in gi2, gi3, gi4, gi5, gi6, gi7:
    pass
# Test globals() with itervalue.
# This is the same as above test, but with a dict comprehension.
di = {i: i for i in ()}
# Test di.itervalue.gi_code.co_code directly.
for i in di.itervalue():
    pass
TestError(TypeError, globals, ())
di = {i: i for i in ()}
di2 = {i: i for i in ()}
di3 = {i: i for i in ()
