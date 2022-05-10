gi = (i for i in ())
# Test gi.gi_code.co_name

gi = (i for i in ())
try:
    gi.gi_code.co_name
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame.f_code.co_name

gi = (i for i in ())
try:
    gi.gi_frame.f_code.co_name
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi_frame.f_lasti

gi = (i for i in ())
try:
    gi.gi_frame.f_lasti
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi_frame.f_lineno

gi = (i for i in ())
try:
    gi.gi_frame.f_lineno
except AttributeError:
    pass
else:
    print('AttributeError expected')
