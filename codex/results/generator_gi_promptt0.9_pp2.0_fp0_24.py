gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_running
# Should return None
print(gi.gi_code, gi.gi_frame, gi.gi_running)

# Test gi.send()
# Should go into StopIteration
try:
  print(gi.send(None))
except StopIteration as e:
  print("StopIteration received:", e.value)
