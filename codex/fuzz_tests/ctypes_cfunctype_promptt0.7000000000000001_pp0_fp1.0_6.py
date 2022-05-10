import ctypes
# Test ctypes.CFUNCTYPE.

# TODO: double, float, restypes, more than one argument

CALLBACK_FUNC = ctypes.CFUNCTYPE(ctypes.c_int)

def callback(value):
    print value
    return 0

print 'Callback:', callback

# call the callback function which has been converted to a c type
callback(1)

# assign the callback to a variable and call it
x = callback
x(2)

# assign the callback to a ctype variable and call it
cb = CALLBACK_FUNC(callback)
cb(3)

# assign the callback to a ctype variable and call it
cb = CALLBACK_FUNC(callback)
print 'Python:', cb
print 'Address:', cb.__int__()
print 'Int address:', ctypes.cast(cb, ctypes.c_void_p).value

# call the callback function which has been converted to a c type
cb(0)

# create a ctype callback, assign it to a ctype variable and call it
def cb1(value):

