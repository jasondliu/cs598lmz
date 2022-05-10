gi = (i for i in ())
# Test gi.gi_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_back.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_back.f_back.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_back.f_back.f_back.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_back.f_back.f_back.f_back.f_code.co_filename
gi.send(None)

# Test gi.gi_frame.f_back.f_back.f_back.f_back.f_back.f_back
