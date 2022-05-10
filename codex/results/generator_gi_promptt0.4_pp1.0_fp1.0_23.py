gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame
print(gi.gi_frame is None)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom is None)

# Test gi.send()
print(gi.send(None))

# Test gi.throw()
try:
    gi.throw(RuntimeError)
except RuntimeError:
    print(True)

# Test gi.close()
gi.close()

# Test gi.gi_frame
print(gi.gi_frame is None)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom is None)

# Test gi.send()
try:
    gi.send(None)
except StopIteration:
    print(True)


