gi = (i for i in ())
# Test gi.gi_code is set to None.
print(gi.gi_code)
# Test gi.gi_frame is set to None.
print(gi.gi_frame)
# Test gi.gi_running is set to False.
print(gi.gi_running)
# Test gi.gi_yieldfrom is set to None.
print(gi.gi_yieldfrom)

# Test __next__ method.
gi = (i for i in range(3))
print(gi.__next__())
print(gi.__next__())
print(gi.__next__())
try:
    gi.__next__()
except StopIteration:
    print('StopIteration')

# Test send method.
gi = (i for i in range(3))
print(gi.send(None))
try:
    gi.send(1)
except TypeError:
    print('TypeError')

# Test throw method.
gi = (i for i in range(3))
try:
    gi.throw(ValueError)
except ValueError:
    print('Value
