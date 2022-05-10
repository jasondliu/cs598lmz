import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# 'utf-16' is available since Python 3.3.
try:
    codecs.decode(b"\xff", "utf-16", "ignore")
except (LookupError, UnicodeDecodeError):
    pass
else:
    # Python 3.6 makes 'utf-16' a cdec.
    codecs.register_error("add_utf16_bytes", add_one_codepoint)
    codecs.register_error("add_utf32_bytes", add_one_codepoint)

# Run PyErr_WriteUnraisable (not PyErr_WriteUnraisableEx) with a non-NULL
# type (not NULL).
#
# We use _PyObject_DebugFree to trigger an invalid free:
# http://bugs.python.org/issue30386.
def callback(exc, v, tb):
    Py_DecRef(v)
    _PyObject_DebugFree(v)

t = PyThreadState_Get()
# This leaks a reference to v: bpo-30386.
PyErr_WriteUnra
