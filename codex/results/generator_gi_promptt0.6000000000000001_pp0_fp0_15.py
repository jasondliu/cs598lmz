gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_frame.f_lasti, gi.gi_frame.f_lineno
# (also test gi.gi_frame.f_trace, but that's not new)
#
# This test is hard to get right, as it has to arrange for the generator
# iterator to be suspended, and then extract the info from its frame.
#
# The tricky part is getting the generator iterator to be suspended.  To do
# that, we arrange for it to be passed to another generator, and then
# iterate over that.  The inner generator iterator has to be passed in
# via a yield, so the outer generator iterator is suspended.

def gen1(gi):
    yield gi.gi_frame.f_lasti
    yield gi.gi_frame.f_lineno

def gen2():
    gi = (i for i in ())
    yield from gen1(gi)
    yield gi.gi_frame.f_lasti
    yield gi.gi_frame.f_lineno

def test_gen_info():
