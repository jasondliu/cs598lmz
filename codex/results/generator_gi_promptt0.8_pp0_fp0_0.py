gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
def f():
    y = gi.gi_code
    z = gi.gi_frame
    return y, z

assert f() == (gi.gi_code, gi.gi_frame)
# Test generator.gi_running
def f():
    gi = (i for i in ())
    assert not gi.gi_running
    assert gi.gi_running == gi.gi_frame is None
    next(gi) # yield 'a'
    assert gi.gi_running
f()
# Test generator.gi_frame.f_lasti
def f():
    one = (i for i in [1])
    zero = (i for i in [0])
    assert one.gi_frame.f_lasti == zero.gi_frame.f_lasti - 1
    assert one.gi_frame.f_lasti == -1
f()
# Test generator.gi_frame.f_lineno
def f():
    gi = (i for i in [0])
    assert gi.gi_
