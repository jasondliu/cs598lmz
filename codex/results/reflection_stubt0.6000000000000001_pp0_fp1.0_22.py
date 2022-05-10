fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__self__ = gi
gi.gi_running = True
gi.gi_frame = fn
gi.gi_code = fn.__code__
gi.gi_frame.f_lasti = -1
gi.gi_frame.f_code = fn.__code__
gi.gi_frame.f_locals = {}

#: The :class:`types.CodeType` object for a generator.
gen_code = gi.gi_code

#: The :class:`types.FrameType` object for a generator.
gen_frame = gi.gi_frame

#: The :class:`types.FunctionType` object for a generator.
gen_func = fn

#: The :class:`types.FunctionType` object for a generator.
gen_func = fn

#: The :class:`types.FunctionType` object for a generator.
gen_func = fn

#: The :class:`types.FunctionType` object for a generator.
gen_func = fn

#: The :class:`
