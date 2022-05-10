gi = (i for i in ())
# Test gi.gi_code.co_flags.
gi.gi_code.co_flags
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test sys.exc_info()
try:
    raise ValueError
except ValueError:
    exc_info = sys.exc_info()
    # Test exc_info[2].tb_frame.f_lasti
    exc_info[2].tb_frame.f_lasti

# Test sys._getframe()
# Test sys._getframe().f_lasti
sys._getframe().f_lasti

# Test sys._current_frames()
# Test sys._current_frames()[thread.get_ident()].f_lasti
sys._current_frames()[thread.get_ident()].f_lasti

# Test threading.current_thread()
# Test threading.current_thread()._frame.f_lasti
threading.current_thread()._frame.f_lasti

# Test sys.settrace()
def tracer(frame, event, arg):
