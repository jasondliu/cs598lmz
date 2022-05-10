gi = (i for i in ())
# Test gi.gi_code.co_filename (should raise RuntimeError)
gi.gi_frame.f_code.co_filename
try:
  
