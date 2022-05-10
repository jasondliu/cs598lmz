gi = (i for i in ())
# Test gi.gi_code == <code object <genexpr> at 0x..., file "<stdin>", line 1>
# Test gi.gi_frame.f_lasti == -1
gi.gi_frame.f_lasti = 0
# Test gi.gi_frame.f_lineno == 1
gi.gi_frame.f_lineno = 2
# Test gi.gi_frame.f_code.co_argcount == 0
gi.gi_frame.f_code.co_argcount = 1
# Test gi.gi_frame.f_code.co_cellvars == ()
gi.gi_frame.f_code.co_cellvars = ('a',)
# Test gi.gi_frame.f_code.co_code == b'd\x01\x00j\x00S'
gi.gi_frame.f_code.co_code = b'd\x02\x00j\x00S'
# Test gi.gi_frame.f_code.co_consts == (None,)
gi.gi_frame.f_code.co
