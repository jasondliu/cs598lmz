gi = (i for i in ())
# Test gi.gi_code.co_argcount
try:
    print(gi.gi_code.co_argcount)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_lineno
try:
    print(gi.gi_frame.f_lineno)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_locals
try:
    print(gi.gi_frame.f_locals)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_frame.f_trace
try:
    print(gi.gi_frame.f_trace)
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.__name__
print(gi.__name__)


