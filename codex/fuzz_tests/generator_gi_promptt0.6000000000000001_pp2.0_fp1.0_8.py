gi = (i for i in ())
# Test gi.gi_code.co_flags.
flags = gi.gi_code.co_flags
print(flags.has_freevars)
print(flags.has_cellvars)
print(flags.generator)
print(flags.no_freevars)
print(flags.no_cellvars)
print(flags.optimized)
print(flags.newlocals)
print(flags.varargs)
print(flags.varkeywords)
print(flags.nested)
print(flags.generator)
print(flags.no_freevars)

# Test gi.gi_frame
frame = gi.gi_frame
print(frame.f_lineno)
print(frame.f_lasti)
print(frame.f_trace)
print(frame.f_exc_traceback)
print(frame.f_exc_type)
print(frame.f_exc_value)
print(frame.f_restricted)
print(frame.f_builtins)
print(frame.f_back)
print(frame.f_tstate)
print(frame
