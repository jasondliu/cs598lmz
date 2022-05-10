gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == CO_COROUTINE

# Test gi.gi_frame
assert gi.gi_frame.f_lasti == 0
assert gi.gi_frame.f_lasti == 0
assert gi.gi_frame.f_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_flags == CO_GENERATOR

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    raise SystemExit("SKIP")

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    raise SystemExit("SKIP")

# Test gi.gi_await
assert gi.gi_await is None

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti = 0
assert gi.gi_frame.f_lasti == 0

# Test that gi
