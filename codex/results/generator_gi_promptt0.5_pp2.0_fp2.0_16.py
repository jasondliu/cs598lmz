gi = (i for i in ())
# Test gi.gi_code is not None.
print(gi.gi_code)
print(gi.gi_code is None)

# Test gi.gi_frame is not None.
try:
    next(gi)
except StopIteration:
    pass
print(gi.gi_frame)
print(gi.gi_frame is None)

# Test gen.gi_running is False.
print(gen.gi_running)

# Test gen.gi_frame is None.
try:
    gen.send(None)
except StopIteration:
    pass
print(gen.gi_frame)
print(gen.gi_frame is None)

# Test gen.gi_code is None.
print(gen.gi_code)
print(gen.gi_code is None)

# Test gen.gi_running is False.
print(gen.gi_running)

# Test gen.gi_frame is None.
try:
    gen.send(None)
except StopIteration:
    pass
print(gen.gi_frame)
print(gen.gi_frame is None)

