gi = (i for i in ())
# Test gi.gi_code
gi = (i for i in range(2))
gi.gi_code = lambda: 23
gi.gi_code()

gi = (i for i in range(2))
try:
    gi.gi_code = 23
except TypeError:
    pass
else:
    print(False)

# Test gi_frame
gi = (i for i in range(2))
gi.gi_frame.f_code = 23
gi.gi_frame.f_code


# Test gi_frame.f_code.co_consts
gi.gi_frame.f_code.co_consts = 23
gi.gi_frame.f_code.co_consts
gi.gi_frame.f_code.co_consts = (None, None, 5)
gi.gi_frame.f_code.co_consts
gi.gi_frame.f_code.co_consts = (None, None, None)


# Test gi_frame.f_code.co_varnames
gi.gi_frame.f_code.co_
