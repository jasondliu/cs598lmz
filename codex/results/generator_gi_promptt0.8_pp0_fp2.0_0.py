gi = (i for i in ())
# Test gi.gi_code
gi.gi_code.co_filename
gi.gi_code.co_name
# Test gi.gi_frame
gi.gi_frame.f_code.co_filename
gi.gi_frame.f_code.co_name
# Test gi.gi_running
gi.gi_running
# Test gi.send
gi.send(42)    #=> 42
gi.send(66)    #=> 66
# Send a StopIteration exception to gi
gi.close()

# Create a new generator
gi2 = (i for i in 'abc')
# Test gi2.gi_code
gi2.gi_code.co_filename
gi2.gi2_code.co_name
# Test gi2.gi_frame
gi2.gi_frame.f_code.co_filename
gi2.gi_frame.f_code.co_name
# Test gi2.gi_running
gi2.gi_running
# Test gi2.send
gi2.send(None) #=> 'a'
gi2.send(None)
