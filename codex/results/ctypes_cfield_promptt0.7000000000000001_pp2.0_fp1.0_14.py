import ctypes
# Test ctypes.CField
assert isinstance(ctypes.CField, type)
assert not hasattr(ctypes.CField, "__dict__")
assert ctypes.CField.__bases__ == (object,)
assert ctypes.CField.__name__ == "CField"

assert isinstance(ctypes.CField.__set_name__, classmethod)
assert isinstance(ctypes.CField.__get__, method)
assert isinstance(ctypes.CField.__set__, method)
assert isinstance(ctypes.CField.__delete__, method)

# Test ctypes.CField.__set_name__
class X:
    a = ctypes.CField()
    b = ctypes.CField()

assert isinstance(X.a, ctypes.CField)
assert hasattr(X.a, "__name__")
assert X.a.__name__ == "a"
assert not hasattr(X.a, "__set_name__")

assert isinstance(X.b, ctypes.CField)
assert hasattr(X.
