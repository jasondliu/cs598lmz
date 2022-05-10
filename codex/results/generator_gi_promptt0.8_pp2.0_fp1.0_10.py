gi = (i for i in ())
# Test gi.gi_code == None
gi_code = None
# Test gi.gi_frame == None
gi_frame = None
# Test gi.gi_running == False
gi_running = False
# Test gi.__name__ == 'genexpr'
# Test gi.__qualname__ == 'genexpr'
# Test gi.__module__ == '__main__'
genexpr = 'genexpr'
# Test gi.gi_frame.f_lasti == -1
f_lasti = -1
# Test gi.gi_frame.f_lineno == 2
f_lineno = 2
# Test gi.gi_frame.f_trace == None
f_trace = None

gi = (i for i in ())
test_support.run_unittest(GetitemTestCase)
