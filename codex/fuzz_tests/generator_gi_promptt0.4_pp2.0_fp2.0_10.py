gi = (i for i in ())
# Test gi.gi_code.co_varnames
try:
    gi.gi_code.co_varnames
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_code.co_varnames
try:
    gi.gi_frame.f_code.co_varnames
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_locals
try:
    gi.gi_frame.f_locals
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_back
try:
    gi.gi_frame.f_back
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_trace
try:
    gi.gi_frame.f_trace
except AttributeError:
    pass
else:
    print('AttributeError expected')


