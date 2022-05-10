gi = (i for i in ())
# Test gi.gi_code


with assert_raises(AttributeError):
    gi.gi_code


# Test gi.gi_running
if gc.isenabled():
    assert test_support.gc_collect() >= 2
    assert gi.gi_running == 0
else:
    gi.gi_running

# Test gi.gi_frame
assert isinstance(gi.gi_frame, types.FrameType)
assert gi.gi_frame.f_code.co_name == 'genexpr'
assert gi.gi_frame.f_lasti > -1


def gen():
    yield
    yield 1


g = gen()
assert g.gi_code is gen.func_code
assert g.gi_frame is None

assert next(g) is None
assert g.gi_frame is not None
assert g.gi_frame.f_lasti > -1
assert g.gi_frame.f_code is gen.func_code


def badgen(x=[]):
    yield
    x.append(1)


g = badgen()

