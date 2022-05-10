gi = (i for i in ())
# Test gi.gi_code (which is different from gi.__code__).
assert gi.gi_code is None
# Test gi.gi_frame
assert gi.gi_frame is None
# test gi.gi_running
assert not gi.gi_running

# Test the API of an iterator on a simple C function.
def test_range():
    it = xrange(5)
    assert isinstance(it.gi_code, types.CodeType)
    # if the function returns to xrange, then the current frame is of
    # xrange or xrange.next.  So we don't have a lot of choices here.
    # skip this check on 2.5+, because the xrange iterator frame is
    # now stopped
    if sys.hexversion < 0x02060000:
        it.next()
        assert it.gi_frame.f_code in (it.gi_code, it.next.__code__)
    else:
        assert it.gi_frame is None
    assert not it.gi_running
    # test normal iterator termination
    list(it)
   
