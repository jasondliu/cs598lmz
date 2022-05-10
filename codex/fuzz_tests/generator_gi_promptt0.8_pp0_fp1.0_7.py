gi = (i for i in ())
# Test gi.gi_code.co_filename
# test_code_filename(gi)

# Test gi.gi_code.co_name
# test_code_name(gi)

# Test gi.gi_frame.f_code.co_filename
# test_frame_filename(gi)

# Test gi.gi_frame.f_code.co_name
# test_frame_name(gi)

li = (i for i in [])
# Test li.gi_code.co_filename
# test_code_filename(li)

# Test li.gi_code.co_name
# test_code_name(li)

# Test li.gi_frame.f_code.co_filename
# test_frame_filename(li)

# Test li.gi_frame.f_code.co_name
# test_frame_name(li)

# Test li.gi_frame.f_locals.items()
test_f_locals_items(li)

# Test li.gi_frame.f_locals.keys()
test_f_
