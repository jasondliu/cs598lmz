gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code.co_name == "", gi.gi_code.co_name
assert gi.gi_code.co_filename == "", gi.gi_code.co_filename
assert gi.gi_frame is None
assert gi.gi_running
assert not gi.gi_cfaced

# gi_code and gi_frame are deallocated and should be None after the generator
# terminates.
def f():
    t = (i for i in ())
    yield 1
    yield 2
    yield t
t = f()
assert t.gi_code.co_name == "f", t.gi_code.co_name
assert t.gi_code.co_filename.endswith("exceptions.py"), (t.gi_code.co_filename, t.gi_code.co_name)
assert t.gi_frame.f_lineno == 13, t.gi_frame.f_lineno
assert t.gi_frame.f_back.f_lineno == 5, t.gi_frame.f_
