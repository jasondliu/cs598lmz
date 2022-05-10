gi = (i for i in ())
# Test gi.gi_code is None
# raises SystemError: iter(<generator object <genexpr> at 0x7f6b38101db0>) returned a result with an error set
#
# Note: A generator in its "finished" state will still have a code object,
# but one that raises StopIteration immediately.
#
gi.gi_code
