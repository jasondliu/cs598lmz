gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test gi.gi_yieldfrom.gi_frame

# Test same generator
gi1 = (i for i in range(10))
gi2 = (i for i in range(10))
gi1.gi_frame.f_lasti
gi2.gi_frame.f_lasti
gi1.gi_frame.f_lasti = 2
gi1.gi_frame.f_lasti
gi2.gi_frame.f_lasti
gi1.gi_frame.f_lasti = 25
gi1.gi_frame.f_lasti
gi2.gi_frame.f_lasti
gi2.gi_frame.f_lasti = -1
gi1.gi_frame.f_lasti
gi2.gi_frame.f_lasti
