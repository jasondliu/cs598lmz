gi = (i for i in ())
# Test gi.gi_code.co_argcount,
# .gi_frame.f_locals, .gi_frame.f_lasti, .gi_frame.f_code.co_code
arg = 1
gi.gi_code.co_argcount == arg
gi.gi_frame.f_locals == locals()
gi.gi_frame.f_lasti == 1
gi.gi_frame.f_code.co_code == b'd\x00\x00' + b'J\x00d\x01\x00\x17\x00d\x02\x00'

gi = (i for i in range(3))
# Test gi.gi_code.co_argcount,
# .gi_frame.f_lasti, .gi_frame.f_code.co_code
arg = 1
gi.gi_frame.f_lasti == 3
gi.gi_frame.f_code.co_code == b'd\x00\x00\x83\x02\x01\x01\x17\x00\x83\x01\x00
