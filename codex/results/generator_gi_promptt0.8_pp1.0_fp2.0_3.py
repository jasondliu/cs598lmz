gi = (i for i in ())
# Test gi.gi_code.co_name for 'gi_code'
#
# PyPy uses '__length_hint__' rather than '__length_code__'
#
# > (Pdb) p gi.__length_hint__.__name__
# '__length_hint__'
# > (Pdb) p gi.gi_code.co_name
# 'gi_code'
#
# Note: gi_frame exists in both CPython 2 & 3 but not PyPy
test_bool(issubclass(type(gi), types.GeneratorType))
test_eq(gi.gi_code.co_name, 'gi_code')
test_eq(gi.gi_frame, None)
test_eq(gi.gi_running, False)
test_eq(gi.gi_yieldfrom, None)
with gi:
    test_eq(gi.gi_running, True)
    test_eq(gi.gi_yieldfrom, None)
test_eq(gi.gi_running, False)
test_eq(gi.gi_yieldfrom,
