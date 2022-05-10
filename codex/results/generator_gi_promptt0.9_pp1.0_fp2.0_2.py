gi = (i for i in ())
# Test gi.gi_code
next(gi)
# Test gi.gi_running
next(gi)
# Test gi.gi_frame
next(gi)
# Test gi.gi_frame.f_locals
next(gi)
# Test gi.gi_frame.f_lasti
next(gi)
# Test gi.gi_frame.f_lineno
next(gi)
# Test gi.gi_frame.f_trace
next(gi)
# Test gi.gi_frame.f_exc_traceback
next(gi)
# Test gi.gi_frame.f_exc_type
next(gi)
# Test gi.gi_frame.f_exc_value
next(gi)
# Test gi.gi_frame.f_restricted
next(gi)
# Test gi.gi_frame.f_builtins
next(gi)
# Test gi.gi_frame.f_back
next(gi)

# Test generator function
def gen(n):
    while n:
        yield n
        n -= 1

[next(
