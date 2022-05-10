gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)

# Test gi.gi_frame
print(gi.gi_frame)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test cr_trace
# This feature is obsolete

# Test gi.cr_await
print(gi.gi_yieldfrom)

# Test gi.cr_frame
print(gi.cr_frame)

# Test gi.cr_running
print(gi.cr_running)

# Test gi.cr_code
print(gi.cr_code)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

class A(object):
    pass

a = A()

gi.gi_frame = a
gi.gi_running = a
gi.gi_yieldfrom = a
gi.gi_code = a
gi.cr_frame = a
gi.cr_running = a
gi.
