gi = (i for i in ())
# Test gi.gi_code
print(type(u.__code__.co_code))
# Test gi.gi_frame
try:
  next(gi)
except StopIteration:
  pass
print(gi.gi_frame.f_code.co_name)
print(gi.gi_frame.f_code.co_filename)
# Test gi.gi_running
gi.gi_running = False
gi.gi_running = True
gi.gi_running = False
gi.gi_running = True
gi.gi_running = False
gi.gi_running = True
gi.gi_running = False
gi.gi_running = True
gi.gi_running = False
gi.gi_running = True
gi.gi_running = None
gi.gi_running = False
gi.gi_running = 1
gi.gi_running = False
gi.gi_running = 2
gi.gi_running = False
gi.gi_running = 3
gi.gi_running = False
print('Done')
