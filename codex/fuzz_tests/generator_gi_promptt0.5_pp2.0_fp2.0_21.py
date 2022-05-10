gi = (i for i in ())
# Test gi.gi_code is None.
print(gi.gi_code)
# Test gi.gi_frame is None.
print(gi.gi_frame)
# Test gi.gi_running is False.
print(gi.gi_running)
# Test gi.gi_yieldfrom is None.
print(gi.gi_yieldfrom)

# Test gi.send(value).
gi = (i for i in range(3))
print(gi.gi_code)
print(gi.gi_frame)
print(gi.gi_running)
print(gi.gi_yieldfrom)
print(gi.send(0))
print(gi.send(1))
print(gi.send(2))
try:
    gi.send(3)
except StopIteration:
    print("StopIteration")

# Test gi.throw(type[, value[, traceback]]).
gi = (i for i in range(3))
print(gi.gi_code)
print(gi.gi_frame)
print(gi.gi_running)
print(gi
