import types
# Test types.FunctionType
def _test_types_FunctionType(f, f2):
    if f.__class__ is not types.FunctionType:
        raise RuntimeError, "%s.__class__ (%s) is not types.FunctionType" % (str(f), f.__class__)
    # Assign to another function
    g = f
    # Assign to other type
    try:
        h = 2 + f
    except TypeError:
        pass
    else:
        raise RuntimeError, "expected TypeError"
    # Assign to function, assigned to implicit local
    try:
        (2 + f2) = f
    except TypeError:
        pass
    else:
        raise RuntimeError, "expected TypeError"
    # Assign to function, assigned to implicit local of for loop
    for _f in (f,):
        try:
            (_f.__class__) = f
        except TypeError:
            pass
        else:
            raise RuntimeError, "expected TypeError"
    # Delete function
    del f
    try:
        del f2
    except
