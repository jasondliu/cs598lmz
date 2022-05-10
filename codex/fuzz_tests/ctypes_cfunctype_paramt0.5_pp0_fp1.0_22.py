import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Function to be called, and its C callback
def py_func(x, y):
  print "x=%d, y=%d" % (x, y)
  return x + y

cb_func = FUNTYPE(py_func)

# Now "integrate" the callback function with the C library
c_lib.set_callback(cb_func)

# Call the C function using the callback
result = c_lib.call_callback(1, 2)
print "result=%d" % result
