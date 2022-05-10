gi = (i for i in ())
# Test gi.gi_code is None
test.test(gi.gi_code is None)
# Test gi.gi_running is False
test.test(gi.gi_running is False)
# Test gi.gi_frame is None
test.test(gi.gi_frame is None)
# Test type(gi.gi_frame) is types.FrameType
test.test(type(gi.gi_frame) is types.FrameType)
# Test gi.gi_yieldfrom is None
test.test(gi.gi_yieldfrom is None)
# Test type(gi.gi_yieldfrom) is types.GeneratorType
test.test(type(gi.gi_yieldfrom) is types.GeneratorType)
# Test gi.gi_name == '<genexpr>'
test.test(gi.gi_name == '<genexpr>')
# Test gi.gi_qualname == '<genexpr>'
test.test(gi.gi_qualname == '<genexpr>')
# Test dir(gi) == ['__class__', '__del__', '__
