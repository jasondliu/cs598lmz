gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send
print(gi.send(None))

# Test gi.throw
try:
    gi.throw(TypeError)
except TypeError:
    print("TypeError")

# Test gi.close
gi.close()

# Test gi.send
try:
    gi.send(None)
except StopIteration:
    print("StopIteration")

# Test gi
