import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a bit of a hack, but it seems to work.
# It's a bit ugly, but it's better than nothing.
# It's also a lot better than the old way, which
# was to use the undocumented _PyObject_GetDictPtr.
# That function is gone in Python 3.2.

def _get_dict(obj):
    """
    Get the dictionary of an object.
    """
    # This is a bit of a hack, but it seems to work.
    # It's a bit ugly, but it's better than nothing.
    # It's also a lot better than the old way, which
    # was to use the undocumented _PyObject_GetDictPtr.
    # That function is gone in Python 3.2.
    return ctypes.cast(id(obj) + object.__basicsize__, ctypes.py_object).value

def _set_dict(obj, d):
    """
    Set the dictionary of an object.
    """
    # This is a bit of a hack, but
