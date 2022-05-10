gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code
gi.gi_code = None
gi.gi_code == None
# Test gi.gi_frame is None
gi.gi_frame
gi.gi_frame == None
# Test gi.gi_running is False
gi.gi_running
gi.gi_running == False
"""

def test_gen_iter_interrupt():
    """
    def gen():
        yield 1
    gi = gen()
    next(gi)
    # Test that gi.gi_running is True
    gi.gi_running
    gi.gi_running == True
    # Test that gi.gi_frame is not None
    gi.gi_frame
    gi.gi_frame != None
    # Test that gi.gi_frame.f_lasti is not None
    gi.gi_frame.f_lasti
    gi.gi_frame.f_lasti != None
    """

def test_gen_iter_finished():
    """
    def gen():
        yield 1
    gi = gen
