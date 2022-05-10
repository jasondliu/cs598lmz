gi = (i for i in ())
# Test gi.gi_code is None
# Test str(gi) is "<genexpr>"
gi = (i for i in ())
# Test gi.gi_code.co_name == "genexpr"
# Test str(gi) is "<genexpr>"
gi = (i for i in ())
# Test gi.gi_code.co_name = "foobar"
# Test str(gi) is "<generator foobar>"
gi = (i for i in ())
# Test gi.gi_frame is None
# Test str(gi) is "<genexpr>"
gi = (i for i in ())
# Test gi.gi_frame.f_locals == {'i':42}
# Test str(gi) is "<genexpr>"
gi = (i for i in ())
# Test gi.gi_frame.f_code.co_name == 'genexpr'
# Test str(gi) is "<generator genexpr>"
gi = (i for i in ())
# Test gi.gi_frame.f_code.co_name = 'foobar'
# Test str(gi) is "<generator
