gi = (i for i in ())
# Test gi.gi_code.co_filename
gi = (i for i in ())
gen_code = gi.gi_code
print(gen_code.co_filename)

# Test gi.gi_frame.f_code.co_filename
gen_frame = gi.gi_frame
print(gen_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_filename
gen_frame = gi.gi_frame
print(gen_frame.f_code.co_filename)

# Test gi.gi_frame.f_lasti
gen_frame = gi.gi_frame
print(gen_frame.f_lasti)

# Test gi.gi_frame.f_lineno
gen_frame = gi.gi_frame
print(gen_frame.f_lineno)

# Test gi.gi_running
# Test gi.gi_yieldfrom
gi = (i for i in ())
print(gi.gi_running)
try:
    gi.gi_yieldfrom
except Attribute
