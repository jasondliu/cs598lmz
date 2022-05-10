gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_localsplus
print(gi.gi_frame.f_localsplus)

# Test gi.gi_frame.f_localsplus[0]
print(gi.gi_frame.f_localsplus[0])

# Test gi.gi_frame.f_localsplus[0].ob_refcnt
print(gi.gi_frame.f_localsplus[0].ob_refcnt)

# Test gi.gi_frame.f_localsplus[1]
print(gi.gi_frame.f_localsplus[1])

# Test gi.gi_frame.f_localsplus[1].ob_refcnt
print(gi.gi_frame.f_localsplus[1].ob_refcnt)

# Test
