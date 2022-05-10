import ctypes
# Test ctypes.CFUNCTYPE()
def callback_func(arg):
    print('Hello World!')

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)

callback = CALLBACK(callback_func)

# Assign to global var
global_callback = callback

# Assign to instance var
class Test(object):
    def __init__(self):
        self.callback = callback

# Assign to local var
def some_func():
    local_callback = callback

# Call from another function
def calling_func(callback):
    callback(42)

# Create a callback from a foreign function
libc = ctypes.CDLL(None)
strlen = libc.strlen
strlen.argtypes = [ctypes.c_char_p]
strlen.restype = ctypes.c_size_t

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def len_callback(s):
    return strlen(s)

