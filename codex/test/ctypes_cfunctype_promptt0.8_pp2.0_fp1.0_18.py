import ctypes
# Test ctypes.CFUNCTYPE:
def call_func(func, args):
    func(*args)

def add_square(x, y):
    print('{} squared is {}'.format(x, x**2))
    return y

CMPFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

call_func(CMPFUNC(add_square), (5, 3))

# Note: The following will not work:
#call_func(add_square, (5, 3))

# CMPFUNC can also be used as a callback for GTK's `connect`:
# (Unfortunately, I don't have GTK installed!)

# windows specific stuff
# TODO: linux stuff

# server stuff

# TODO: use sockets to send data from multiple clients to a single server

# TODO: send recieve data between multiple servers and multiple clients

# web stuff

