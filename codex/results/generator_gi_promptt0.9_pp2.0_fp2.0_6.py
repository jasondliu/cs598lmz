gi = (i for i in ())
# Test gi.gi_code.co_code, gi.gi_frame.f_code.co_code
# (g_frame.f_code.co_code = gi.gi_code.co_code)
assert gi.gi_code.co_code == b''
assert gi.gi_frame.f_code.co_code == b''

gi = (i for i in [1, 2, 3, 4])
# Test gi.gi_code.co_code, gi.gi_frame.f_code.co_code
# (g_frame.f_code.co_code = gi.gi_code.co_code)
assert gi.gi_code.co_code == (
    b'|\x00|\x01\x17\x00|\x02\x17\x00\x17\x00}\x00|\x00\x83\x01\x01'
    b'|\x01d\x01}\x00|\x00\x83\x01\x01|\x01d\x01}\x00
