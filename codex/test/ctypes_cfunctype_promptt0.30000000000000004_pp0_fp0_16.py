import ctypes
# Test ctypes.CFUNCTYPE

# This is a C function that takes a callback as an argument
# and calls it with a string.

CALLBACK_PROTO = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

def callback(s):
    print('callback called with:', s)

def call_callback(callback_func):
    callback_func(b'hello world')

# Convert the Python function to a C callback

c_callback = CALLBACK_PROTO(callback)

# Call the C function with the callback

call_callback(c_callback)

# This prints:
#
# callback called with: b'hello world'
#
# Note that the callback is called with a bytes object, not a string.
# This is because the C function is declared to take a char*, not a
# Python object.

# Now try calling the callback from another thread.

import threading

threading.Thread(target=call_callback, args=(c_callback,)).start()

# This prints:
#
# callback called with: b'hello world
