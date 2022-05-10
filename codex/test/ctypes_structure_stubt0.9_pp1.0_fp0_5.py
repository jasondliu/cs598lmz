import ctypes

class S(ctypes.Structure):
    x = 0

def foo(obj):
    if not isinstance(obj, ctypes.Structure) or len(obj._fields_) != 1:
        raise AssertionError("not equal")

def main():
    foo(S())
