gi = (i for i in ())
# Test gi.gi_code
gj = gi.gi_code
# Test gj.co_name
gk = gj.co_name
# Test gk.__length_hint__
gl = gk.__length_hint__

# Test gi.gi_frame
gm = gi.gi_frame
# Test gm.f_back
gn = gm.f_back
# Test gm.f_code.co_name
go = gm.f_code.co_name
# Test gm.f_code.co_name
gp = gm.f_code.co_name
# Test gm.f_lineno
gq = gm.f_lineno

# test gi.gi_running
gr = gi.gi_running

# test gi.gi_frame.f_locals
gs = gi.gi_frame.f_locals
