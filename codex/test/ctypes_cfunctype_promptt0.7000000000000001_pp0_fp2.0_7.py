import ctypes
# Test ctypes.CFUNCTYPE
# The functions we will call

def my_callback(a: int, b: int) -> int:
    """Return a*b."""
    return a * b

def my_callback_exception(a: int, b: int) -> int:
    """Raise an exception."""
    raise Exception("my_callback_exception")

