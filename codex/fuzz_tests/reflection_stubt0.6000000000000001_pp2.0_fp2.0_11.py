fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_code = fn
gi.gi_frame = fn
gi.gi_running = True
gi.gi_next = fn
gi.gi_frame = fn
gi.gi_frame.f_lasti = 0
gi.gi_frame.f_lineno = 0
gi.gi_frame.f_builtins = {}
gi.gi_frame.f_globals = {}
gi.gi_frame.f_locals = {}
gi.gi_frame.f_trace = None
gi.gi_frame.f_exc_traceback = None
gi.gi_frame.f_exc_type = None
gi.gi_frame.f_exc_value = None
