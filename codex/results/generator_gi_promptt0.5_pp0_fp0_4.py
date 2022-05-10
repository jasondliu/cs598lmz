gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)

# Test gi.gi_frame
def g():
    yield 1
    yield 2

gi = g()
print(gi.gi_frame.f_lasti)
print(gi.gi_frame.f_lineno)

# Test gi.gi_running
def g():
    yield 1
    yield 2

gi = g()
print(gi.gi_running)
print(next(gi))
print(gi.gi_running)
print(next(gi))
print(gi.gi_running)

# Test gi.gi_frame.f_locals
def g():
    yield 1
    x = 2
    yield x

gi = g()
print(gi.gi_frame.f_locals)
print(next(gi))
print(gi.gi_frame.f_locals)
print(next(gi))
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_glob
