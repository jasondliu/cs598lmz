import ctypes
ctypes.cast(x, ctypes.py_object).value = y
</code>
Or, if you want to see what <code>ctypes</code> module is doing, you can look at its source code:
<code>def cast(obj, typ, from_ptr=False):
    """Casts a ctypes instance into a ctypes pointer of the given type.

    Supported are integer values and ctypes instances.
    For integer values the address of the parameter passed in is used.
    """
    if isinstance(obj, (int, long)):
        return typ.from_address(obj)
    if isinstance(obj, _CData):
        if from_ptr:
            return obj
        return obj._as_parameter_
    if isinstance(obj, basestring):
        raise TypeError("Wrong type")
    if hasattr(obj, '_as_parameter_'):
        return obj._as_parameter_
    raise TypeError("Wrong type")
</code>

