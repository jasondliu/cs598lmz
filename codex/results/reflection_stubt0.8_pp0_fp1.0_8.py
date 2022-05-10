fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.gi_frame.f_code
gi.gi_frame.f_trace = fn
gi.gi_frame.f_back = None
gi.gi_frame.f_lineno = 0
gi.gi_running = False
gi.gi_frame.f_lasti = -1
gi.gi_frame.f_exc_traceback = None
gi.gi_frame.f_exc_type = None
gi.gi_frame.f_exc_value = None
