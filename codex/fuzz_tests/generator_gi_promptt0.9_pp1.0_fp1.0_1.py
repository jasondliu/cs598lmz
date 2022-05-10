gi = (i for i in ())
# Test gi.gi_code
gi.gi_code  # EOFError

# Test return gi.gi_code
gi.gi_code  # EOFError

gi = (i for i in (1,2,3))

gi.gi_code  # _make_gen
gi.gi_frame.f_lasti  # 0
gi.gi_frame.f_locals  # {'i': 1}
gi.gi_frame.f_code.co_filename  # <stdin>
gi.gi_frame.f_code.co_name  # '<genexpr>'
gi.gi_frame.f_code.co_firstlineno  # __future__ line
gi.gi_frame.f_back  # None

gi.gi_frame.f_code.co_argcount  # 0
gi.gi_frame.f_code.co_varnames  # ('i',)
gi.gi_frame.f_code.co_stacksize  # 2
gi.gi_frame.f_code.co_flags  # 0x0010
gi.gi
