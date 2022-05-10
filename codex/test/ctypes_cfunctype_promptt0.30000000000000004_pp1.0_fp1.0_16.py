import ctypes
# Test ctypes.CFUNCTYPE()

# This is an example of a function with a callback.
# The callback takes a string and returns an integer.

# This is the function that takes the callback.
def function_with_callback(callback):
    # Call the callback with a string.
    return callback("Hello, World!")

# This is the callback.
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def callback_func(string):
    # Print the string.
    print(string)

    # Return an integer.
    return 42

# Call the function with the callback.
