import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()

# Check that the values are what we expect
assert s.x == 1
assert s.y == 2

# Check that we can assign to the fields
s.x = 3
s.y = 4

# Check that the values are what we expect
assert s.x == 3
assert s.y == 4

# Check that we can assign to the fields
s.x = 5
s.y = 6

# Check that the values are what we expect
assert s.x == 5
assert s.y == 6

print('ok')
