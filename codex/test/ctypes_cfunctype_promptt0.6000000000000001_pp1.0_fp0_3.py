import ctypes
# Test ctypes.CFUNCTYPE
def test_with_doc(x):
    """test_with_doc(x) -> None

    test function with docstring
    """
    return x

class X(object):
    def __init__(self):
        self.a = 1
    def f(self):
        return "f"

class Y(object):
    def __init__(self):
        self.a = 1
    def f(self):
        return "g"

def test_with_closure(x):
    """test_with_closure(x) -> None

    test function with closure
    """
    def closure():
        return x
    return closure

def test_with_defaults(x, y=1, z=2):
    """test_with_defaults(x [,y=1 [,z=2]]) -> None

    test function with default args
    """
    return x

# Test ctypes.PYFUNCTYPE
