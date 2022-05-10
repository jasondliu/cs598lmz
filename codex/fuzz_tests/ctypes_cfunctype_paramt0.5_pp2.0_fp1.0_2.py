import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# Register a callback function.
def register_callback(function):
    global _callback
    _callback = FUNTYPE(function)
    _lib.register_callback(_callback)

# Register a callback function.
def register_callback_with_arg(function):
    global _callback
    _callback = FUNTYPE(function)
    _lib.register_callback_with_arg(_callback)

# Register a callback function.
def register_callback_with_arg_and_return(function):
    global _callback
    _callback = FUNTYPE(function)
    _lib.register_callback_with_arg_and_return(_callback)

# Call the callback function.
def call_callback():
    _lib.call_callback()

# Call the callback function.
def call_callback_with_arg(arg):
    _lib.call_callback_with_arg(arg)

# Call the callback function.
def call_callback_with_arg_and_return(arg):
    return _lib.call_callback_with_arg_and_return(arg)

