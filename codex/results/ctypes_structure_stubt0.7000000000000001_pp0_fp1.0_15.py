import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

# copy the data from a list of tuples
s = S()
s.x, s.y, s.z = [1,2,3]

# copy the data to a list of tuples
t = [s.x, s.y, s.z]
</code>

