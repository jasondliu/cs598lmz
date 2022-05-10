gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_code.co_filename
print(gi.gi_code.co_filename)
# Test gi.gi_code.co_argcount
print(gi.gi_code.co_argcount)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)

# Test getgeneratorlocals()
gi = (i for i in ())
gl = gi.gi_frame.f_locals
print(getgeneratorlocals(gi) == gl)

# Test getgeneratorstate()
gi = (i for i in ())
print(getgeneratorstate(gi) == 'GEN_CREATED')
gi.__next__()
print(getgeneratorstate(gi) == 'GEN_SUSPENDED')
gi.close()
print(getgeneratorstate(gi
