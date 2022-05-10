gi = (i for i in ())
# Test gi.gi_code
test_gi = generatorexp.newcall(generatorexp, generatorexp.co_code, tuple)
assert test_gi(1, 3) == (1, 3)
assert test_gi().gi_code is generatorexp.co_code

# Test gi.gi_running
assert test_gi(2, 3).gi_running == False

# Test gi.gi_frame
assert isinstance(test_gi(3, 3).gi_frame, FunctionFrameType)

# Test gi.gi_yieldfrom
def yfi():
    yield Test gi_yieldfrom
for i in yfi():
    assert i == "Test gi_yieldfrom"

# Test generator.gi_frame.f_lasti
# assert test_gi(1, 3, 5, 7).gi_frame.f_lasti >= 0

# Test generator.gi_frame.f_back
assert test_gi(1, 3, 5, 7).gi_frame.f_back is None

# Test generator.gi_frame.f_trace
