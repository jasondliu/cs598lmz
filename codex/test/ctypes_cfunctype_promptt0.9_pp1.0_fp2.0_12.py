import ctypes
# Test ctypes.CFUNCTYPE
TYPES = ['double', 'i', 'd', 'i']

def cfunc(a, b, c, d):
    """cfunc: (a: float, b: float, c: float, d: float) -> float"""
    return float(len(TYPES))

C = ctypes.CFUNCTYPE
