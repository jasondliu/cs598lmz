import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Function to be called through the API
def myCallback(x, y, z, a, b):
    print("myCallback called")
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("a:", a)
    print("b:", b)
    return

# API function
def setCallback(callback):
    print("setCallback called")
    # do some stuff with the callback
    callback(1, 2, 3, 4, 5)
    return

# Functype for the callback
callback = FUNTYPE(myCallback)
callback(1, 2, 3, 4, 5)

# Call the API function
setCallback(callback)
</code>

