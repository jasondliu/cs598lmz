import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Python 2.x
if sys.version_info[0] == 2:
    def make_callback(func):
        return FUNTYPE(func)

# Python 3.x
else:
    def make_callback(func):
        return FUNTYPE(func)

# Load the library
lib = ctypes.CDLL('./libfoo.so')

# Define the callback function
@make_callback
def callback(x):
    print('Callback called with value:', x)
    return x + 1

# Register the callback
lib.register_callback(callback)

# Call the function that calls the callback
lib.call_callback(1)
</code>

