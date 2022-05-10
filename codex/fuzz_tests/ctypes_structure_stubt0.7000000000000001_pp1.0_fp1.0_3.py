import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

# Create an instance of S
s = S()
# Create an instance of S and initialize the x field,
# the y field is initialized to 0.
s = S(x=10)
# Create an instance of S and initialize both the x and y fields.
s = S(x=10, y=20)
# Create an instance of S and initialize the x field,
# the y field is left uninitialized.
s = S(x=10, y=None)
# Create an instance of S and initialize both the x and y fields.
s = S(10, 20)
# Create an instance of S and initialize the x field,
# the y field is initialized to 0.
s = S(10, None)
# Create an instance of S and initialize the x field,
# the y field is left uninitialized.
s = S(10)
# Create an instance of S and initialize the x field,
# the y field is initialized to 0.
s = S(*[10])
# Create an instance of S and initialize both the
