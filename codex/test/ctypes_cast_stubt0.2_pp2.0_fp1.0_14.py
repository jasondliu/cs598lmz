import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the only way to detect whether the current Python
# interpreter supports the buffer protocol.
try:
    memoryview(b"")
except TypeError:
    def _check_byteslike(obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj
        raise TypeError("expected bytes-like object, not %s" % type(obj).__name__)
else:
    memoryview(bytearray(b""))
    def _check_byteslike(obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj
        if isinstance(obj, memoryview):
            return obj.tobytes()
        raise TypeError("expected bytes-like object, not %s" % type(obj).__name__)

def _check_unicode(data):
    if isinstance(data, str):
        return data
    raise TypeError("expected unicode object, not %s" % type(data).__name__)

