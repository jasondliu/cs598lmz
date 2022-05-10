gi = (i for i in ())
# Test gi.gi_code is None
# Test gi.gi_frame is None
# Test gi.gi_running is False

gi = (i for i in range(10))
# Test gi.gi_code is not None
# Test gi.gi_frame is not None
# Test gi.gi_running is False

gi.gi_frame.f_lasti = -1
gi.gi_frame.f_back = None
# Test gi.gi_running is False

gi.gi_frame.f_lasti = 0
gi.gi_frame.f_back = None
# Test gi.gi_running is True

gi.gi_frame.f_lasti = 0
gi.gi_frame.f_back = FrameType(None, None, None, None)
# Test gi.gi_running is True

gi.gi_frame.f_lasti = -1
gi.gi_frame.f_back = FrameType(None, None, None, None)
# Test gi.gi_running is False

# Test gi.gi_code is None after
