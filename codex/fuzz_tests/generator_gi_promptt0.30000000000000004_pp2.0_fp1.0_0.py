gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_trace
def f():
    yield 1

gi = f()
print(gi.gi_frame.f_trace)

# Test gi.gi_frame.f_trace_lines
def f():
    yield 1

gi = f()
print(gi.gi_frame.f_trace_lines)

# Test gi.gi_frame.f_trace_opcodes
def f():
    yield 1

gi = f()
print(gi.gi_frame.f_trace_opcodes)

# Test gi.gi_frame.f_lineno
def f():
    yield 1

gi = f()
print(gi.gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti
def f():
    yield 1

gi = f()
