import gc, weakref

# import config

def as_bytes(s):
    return s.encode("utf-8") if isinstance(s, str) else s

def as_unicode(s):
    return s.decode("utf-8") if isinstance(s, bytes) else s

def as_str(s):
    return as_unicode(s) if isinstance(s, bytes) else s

def wrap_bytes(s):
    if isinstance(s, str):
        return s.encode("utf-8")
    elif isinstance(s, bytes):
        return s
    else:
        raise TypeError("Expected str or bytes, got %r" % s)

def wrap_unicode(s):
    if isinstance(s, str):
        return s
    elif isinstance(s, bytes):
        return s.decode("utf-8")
    else:
        raise TypeError("Expected str or bytes, got %r" % s)

