fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# StackFrameObject
sf = _get_stack_frame(fn)
assert sf.f_code == gi.gi_code
assert sf.f_globals == fn.__globals__

# TracebackObject
tb = _get_traceback(fn)
assert tb.tb_frame == sf
assert tb.tb_lineno == 1
assert tb.tb_next is None
assert tb.tb_lasti == -1
assert tb.tb_trace is None
assert tb.tb_lineno == 1
assert tb.tb_frame.f_code == gi.gi_code

# FrameInfo
fi = _get_frame_info(fn, tb)
assert fi.filename == gi.gi_code.co_filename
assert fi.function == gi.gi_code.co_name
assert fi.lineno == 1
assert fi.index == -1
assert fi.current_line is None

# CodeObject
co = _get_code
