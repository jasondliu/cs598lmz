import ctypes
# Test ctypes.CFUNCTYPE
#   This defines a function pointer type and then calls it.
#   The call passes string arguments and receives a string result.
#   The result string is freed.

# Create a prototype for a function pointer, and a variable to hold the address
callback_prototype = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
callback = callback_prototype()

# Define a callback function and assign its address to the variable
@callback_prototype
def my_callback(string1, string2):
    print("My callback has been called with arguments:")
    print(string1)
    print(string2)
    string3 = ctypes.create_string_buffer(len(string1) + len(string2) + 1)
    string3.value = bytes(string1, 'utf-8') + bytes(string2, 'utf-8')
    return string3.value

callback.value = my_callback

# Call the callback
result = callback("Hello", " World")
print("The result
