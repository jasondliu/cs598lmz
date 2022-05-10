gi = (i for i in ())
# Test gi.gi_code = None
inspect.getcoroutinestate(gi)
gi = (i for i in [])
# Test gi.gi_frame = None
inspect.getcoroutinestate(gi)

gi = (i for i in [])
gi.gi_frame.gi_code = None
inspect.getcoroutinestate(gi)
gi = (i for i in [])
gi.gi_frame.f_lasti = None
inspect.getcoroutinestate(gi)

gi = (i for i in [])
gi.gi_frame.f_code.co_flags &= ~0x80
inspect.getcoroutinestate(gi)

gi = (i for i in [])
gi.gi_frame.f_lasti = -1
inspect.getcoroutinestate(gi)
gi = (i for i in [])
gi.gi_frame.f_lasti = 999
inspect.getcoroutinestate(gi)

gi = (i for i in [])
gi.gi_frame.f_lasti =
