gi = (i for i in ())
# Test gi.gi_code is a function
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)

# Test gi.gi_running is 0
print(gi.gi_running)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

print('\n')

# Test gi.gi_yieldfrom.gi_code is a function
print(gi.gi_yieldfrom.gi_code)
# Test gi.gi_yieldfrom.gi_frame is None
print(gi.gi_yieldfrom.gi_frame)

# Test gi.gi_yieldfrom.gi_running is 0
print(gi.gi_yieldfrom.gi_running)

# Test gi.gi_yieldfrom.gi_yieldfrom is None
print(gi.gi_yieldfrom.gi_yieldfrom)

print()

# Test gi.gi_yieldfrom.gi_yieldfrom.gi_code is a function
print(gi.
