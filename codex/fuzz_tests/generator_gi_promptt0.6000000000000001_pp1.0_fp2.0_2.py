gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)

# Test gi.gi_frame.f_code.co_firstlineno
print(gi.gi_frame.f_code.co_firstlineno)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)

'''

# Test module.__file__
print(__file__)

# Test module.__name__
print(__name__)

# Test module.__package__
print(__package__)

# Test module.__spec__
print(__spec__)
