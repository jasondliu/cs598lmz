gi = (i for i in ())
# Test gi.gi_code is a function
test.test(isinstance(gi.gi_code, types.FunctionType))

# Test that gi.gi_code is the same as the function we pass into the
# generator expression
test.test(gi.gi_code is genExprFunc)

# Test that gi.gi_frame is not None
test.test(gi.gi_frame is not None)

# Test that gi.gi_frame.f_code is the same as gi.gi_code
test.test(gi.gi_frame.f_code is gi.gi_code)

# Test that gi.gi_frame.f_lasti is set to the instruction that
# produces the stopiteration exception
test.test(gi.gi_frame.f_lasti == gi.gi_code.co_code.find(b"\x53"))

# Test that gi.gi_frame.f_locals is set to the locals of the
# generator expression
test.test(gi.gi_frame.f_locals == genExprFunc.__code
