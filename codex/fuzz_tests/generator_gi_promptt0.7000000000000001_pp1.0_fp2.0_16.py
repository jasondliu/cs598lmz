gi = (i for i in ())
# Test gi.gi_code.co_name
print(f'{gi.gi_code.co_name}')
# Test gi.gi_frame.f_code.co_name
print(f'{gi.gi_frame.f_code.co_name}')
# Test gi.gi_frame.f_code.co_filename
print(f'{gi.gi_frame.f_code.co_filename}')
# Test gi.gi_frame.f_code.co_firstlineno
print(f'{gi.gi_frame.f_code.co_firstlineno}')
# Test gi.gi_frame.f_locals
print(f'{gi.gi_frame.f_locals}')

# Test gi.gi_frame.f_globals
print(f'{gi.gi_frame.f_globals}')
