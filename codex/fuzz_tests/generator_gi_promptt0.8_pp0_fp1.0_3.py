gi = (i for i in ())
# Test gi.gi_code
print(code_obj.co_code[gi.gi_frame.f_lasti])
print(code_obj.co_code[gi.gi_frame.f_lasti:])
# Test gi.gi_frame.f_lasti
print("{} {} {}".format(
    gi.gi_frame.f_lasti,
    gi.gi_frame.f_lasti + 1,
    gi.gi_frame.f_lasti + 2,
))

# Test gi.gi_frame.f_lasti + 1
print("{} {} {}".format(
    gi.gi_frame.f_lasti + 1,
    gi.gi_frame.f_lasti + 2,
    gi.gi_frame.f_lasti + 3,
))

# Test gi.gi_frame.f_lasti + 2
print("{} {} {}".format(
    gi.gi_frame.f_lasti + 2,
    gi.gi_frame.f_lasti + 3,
   
