gi = (i for i in ())
# Test gi.gi_code
print(g0.gi_code)
print(g1.gi_code)
print(g0.gi_code.co_name == 'stop')
print(g1.gi_code.co_name == 'stop')
# Test gi.gi_frame
print(g0.gi_frame)
print(g1.gi_frame)
print(g0.gi_frame == None)
print(g1.gi_frame == None)
# Test gi.gi_frame.f_code.co_name
print(g0.gi_frame.f_code.co_name == '')
print(g1.gi_frame.f_code.co_name == '_[1]')
# Test gi.gi_frame.f_code.co_filename
print(g0.gi_frame.f_code.co_filename == '<range_iterator>')
print(g1.gi_frame.f_code.co_filename == '<compiled code>')

# Create generators to test 'gi_frame'
l0 = [i for i
