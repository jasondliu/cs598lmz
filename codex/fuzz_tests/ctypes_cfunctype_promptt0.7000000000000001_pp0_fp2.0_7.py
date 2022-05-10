import ctypes
# Test ctypes.CFUNCTYPE
# The functions we will call

def my_callback(a: int, b: int) -> int:
    """Return a*b."""
    return a * b

def my_callback_exception(a: int, b: int) -> int:
    """Raise an exception."""
    raise Exception("my_callback_exception")

@my_callback.ctypes_function
def my_callback_ctypes(a: int, b: int) -> int:
    """Return a*b (test ctypes_function decorator)."""
    return a * b

@my_callback_exception.ctypes_function
def my_callback_exception_ctypes(a: int, b: int) -> int:
    """Raise an exception (test ctypes_function decorator)."""
    raise Exception("my_callback_exception_ctypes")

# Some tests
def test_CFUNCTYPE() -> None:
    assert ctypes.CFUNCTYPE(None)(lambda: None)() is None

    assert ctypes.CFUNCTYPE
