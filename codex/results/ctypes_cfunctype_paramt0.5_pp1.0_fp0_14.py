import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def create_function(name, argtypes, restype, doc=None):
    """
    Creates a new function object and registers it in the global
    environment.
    """
    # Create the function object
    func = FUNTYPE((name, globals()), argtypes, restype)
    # Register the function
    globals()[name] = func
    # Set the docstring
    if doc:
        func.__doc__ = doc
    return func

# Create the function
create_function("my_function", [ctypes.c_int], ctypes.c_int,
                "A simple function")
</code>

