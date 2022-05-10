import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack around the fact that ctypes objects are not weak referencable
_ctypes_hack = weakref.WeakKeyDictionary()

def _ctypes_from_outparam(outparam):
    if outparam is None:
        return None
    else:
        return _ctypes_hack.setdefault(outparam, ctypes.cast(id(outparam), ctypes.py_object).value)

def _outparam_from_ctypes(outparam):
    if outparam is None:
        return None
    else:
        return ctypes.cast(id(outparam), ctypes.py_object).value

def _ctypes_from_value(value):
    if value is None:
        return None
    elif isinstance(value, ctypes.Array):
        return value
    elif isinstance(value, (int, long)):
        return ctypes.c_int(value)
    elif isinstance(value, float):
        return ctypes.c_double(value)

