import _struct

def PyInit_sse2():
    """Initialize the 'sse2' module."""
    _init_Python_API()
    module = _pymodule_new("sse2")
    _PyModule_AddObject(module, "c", _pymodule_new_c())
    return module
