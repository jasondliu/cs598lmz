gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test inspect.getargspec()
def f(a, b, c=1, d=2, *e, **f): pass
print(inspect.getargspec(f))

# Test inspect.getcallargs()
print(inspect.getcallargs(f, 1, 2, 3, 4, 5, 6, 7, 8))

# Test inspect.getclosurevars()
def f(a, b, c=1, d=
