import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def func_pointer(f):
    return FUNTYPE(f)

# This is a test function to be called by the callback
def test_func(x):
    print x

# Create a callback function
test_func_ptr = func_pointer(test_func)

# Create a test callback
test_callback = callback(test_func_ptr)

# Call the function
test_callback(5)
</code>
The output is:
<code>5
</code>

