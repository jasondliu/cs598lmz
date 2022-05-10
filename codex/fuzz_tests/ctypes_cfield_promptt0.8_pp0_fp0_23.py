import ctypes
# Test ctypes.CFields
def CFields(self=None):
    class S(Structure):
        _fields_ = [("x", c_int), ("y", c_int)]
    assert hasattr(S, 'x') == 1 and hasattr(S, 'y') == 1

# Test ctypes.CFUNCTYPES
def CFUNCTYPES(self=None):
    # Issue #1072: a bug with marshalling in callback functions:
    # Python => C => Python
    proto = CFUNCTYPE(c_int, c_char_p)
    def func(arg):
        if platform.python_implementation() == "PyPy":
            # pygame compatibility
            return len(arg.__buffer__)
        if sys.version_info[0] >= 3:
            return len(arg.encode())
        return len(arg)
    cb = proto(func)
    # ctypes.call_function is used in _ctypes_test
    assert ctypes.call_function(proto, cb, "abc") == 3

def c_buffer
