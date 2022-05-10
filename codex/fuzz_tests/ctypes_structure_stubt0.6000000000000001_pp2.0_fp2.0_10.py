import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

accelerometer = ctypes.CDLL('./accelerometer.so')
accelerometer.init()

# Set up the return type and argument types
accelerometer.get_data.restype = S
accelerometer.get_data.argtypes = []

# Call the function
s = accelerometer.get_data()
print s.x, s.y, s.z

# Clean up
accelerometer.cleanup()
