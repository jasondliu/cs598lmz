gi = (i for i in ())
# Test gi.gi_code (code, name, filename, lineno, lnotab, freevars)
assert gi.gi_code == (False, '<genexpr>', __file__, 5, b'', ())
# Test gi.gi_frame (frame, lasti, stack[], locals,
#                    builtins, globals, code, outstanding,
#                    blockstack[])
frame = gi.gi_frame
assert frame.f_lasti == -1
assert frame.f_stacktop is None
assert frame.f_stack == ()
assert frame.f_locals == {'i': '<genexpr>'}
assert frame.f_builtins is __builtins__
assert frame.f_globals is globals()
assert frame.f_code is gi.gi_code
assert frame.f_exc_type is None
assert frame.f_exc_value is None
assert frame.f_exc_traceback is None
assert frame.f_back is None
assert frame.f_blockstack == ()

# Test gi.gi_running
gi.gi_running =
