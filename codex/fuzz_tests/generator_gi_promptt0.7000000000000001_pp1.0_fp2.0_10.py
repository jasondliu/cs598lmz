gi = (i for i in ())
# Test gi.gi_code
if gi.gi_code.co_name != '<genexpr>':
    print('Failed: co_name should be "<genexpr>"')
# Test gi.gi_frame
if gi.gi_frame.f_code.co_name != '<genexpr>':
    print('Failed: f_code.co_name should be "<genexpr>"')
# Test gi.gi_frame.f_locals
if gi.gi_frame.f_locals is not None:
    print('Failed: f_locals should be None')
# Test gi.gi_frame.f_lasti
if gi.gi_frame.f_lasti == -1:
    print('Failed: f_lasti should be >= 0')
# Test gi.gi_frame.f_lineno
if gi.gi_frame.f_lineno == -1:
    print('Failed: f_lineno should be >= 0')
# Test gi.gi_frame.f_trace
if gi.gi_frame.f_trace is
