import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class A(S):
    pass

class B(S):
    pass

class C(A, B):
    pass

class D(B, A):
    pass

class E(C, D):
    pass

assert E.x == E.__base__.__base__.__base__.__base__.x
assert E.x == E.__base__.__base__.__base__.__base__.__base__.__base__.x
assert E.x == E.__base__.__base__.__base__.__base__.__base__.__base__.__base__.x
assert E.x == E.__base__.__base__.__base__.__base__.__base__.__base__.__base__.__base__.x
assert E.x == E.__base__.__base__.__base__.__base__.__base__.__base__.__base__.__base__.__base__.x

assert E.x == E.__b
