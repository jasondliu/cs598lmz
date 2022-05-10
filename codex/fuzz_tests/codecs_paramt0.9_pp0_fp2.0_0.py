import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def is_str(x):
    """
    Check if input is of basestring type.
    We exclude numpy strings here because they do not support u""
    """
    if type(x) == _np.unicode_:
        return True
    elif type(x) == _np.string_:
        return False
    else:
        return isinstance(x, basestring)

def encode_string(x):
    """Encode string -> unicode, bytes -> str"""
    # this will fail for numpy strings, but we don't need it there
    if isinstance(x, basestring):
        if x is None:
            return None
        else:
            return x.decode('utf-8', 'replace_with_space')
    else:
        raise ValueError("Unsupported type: %s" % type(x))

def nsplit(arr, n):
    i = 0
    while i < arr.shape[0]:
        yield arr[
