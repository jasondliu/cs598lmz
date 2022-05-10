from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("">")

def _Fp_add(x, y):
    return x + y
s._Fp_add = _Fp_add

def _Fp_sub(x, y):
    return x - y
s._Fp_sub = _Fp_sub

def _Fp_mul(x, y):
    return x * y
s._Fp_mul = _Fp_mul

def _Fp_rshift(a, b):
    a >>= b
    if a >= P:
        a -= P
    return a
s._Fp_rshift = _Fp_rshift

def _Fp_lshift(a, b):
    return (a << b) % P
s._Fp_lshift = _Fp_lshift

def _Fp_invert(x):
    return pow(x, P - 2, P)
s._Fp_invert = _Fp_invert


def _Fp_square(x):
    return pow(x
