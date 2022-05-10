gi = (i for i in ())
# Test gi.gi_code.co_flags
print(g.gi_code.co_flags)
# Test gi.gi_frame.f_code.co_flags
print(g.gi_frame.f_code.co_flags)

# Test gi.gi_frame.f_locals
print(g.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
def traceit(frame, event, arg):
    print(event)
    return traceit
g = (i for i in ())
g.gi_frame.f_trace = traceit
next(g)

# Test gi.gi_frame.f_trace
def traceit(frame, event, arg):
    print(event)
    return traceit
g = (i for i in ())
g.gi_frame.f_trace = traceit
next(g)

# Test gi.gi_frame.f_trace_opcodes
def traceit(frame, event, arg):
    print(event)
    return traceit
g = (i for i in ())

