import ctypes
# Test ctypes.CFUNCTYPE

def func(x):
    return x + 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)

assert f(1) == 2
assert f(2) == 3
assert f(3) == 4
assert f(4) == 5
assert f(5) == 6
assert f(6) == 7
assert f(7) == 8
assert f(8) == 9
assert f(9) == 10
assert f(10) == 11
assert f(11) == 12
assert f(12) == 13
assert f(13) == 14
assert f(14) == 15
assert f(15) == 16
assert f(16) == 17
assert f(17) == 18
assert f(18) == 19
assert f(19) == 20
assert f(20) == 21
assert f(21) == 22
assert f(22) == 23
assert f(23) == 24
assert f(24) == 25
assert f(25) == 26
assert f(26) == 27
assert f(
