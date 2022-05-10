import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def test_fibonacci():
    fib = FUNTYPE(fibonacci)
    assert fib(0) == 0.0
    assert fib(1) == 1.0
    assert fib(2) == 1.0
    assert fib(3) == 2.0
    assert fib(4) == 3.0
    assert fib(5) == 5.0
    assert fib(6) == 8.0
    assert fib(7) == 13.0
    assert fib(8) == 21.0
    assert fib(9) == 34.0
    assert fib(10) == 55.0
    assert fib(11) == 89.0
    assert fib(12) == 144.0

def test_fibonacci_n():
    fibn = FUNTYPE(fibonacci_n)
    assert fibn(0) == 0.0
    assert fibn(1) == 1.0
    assert fibn(2) == 1.0
    assert fibn(3) == 2.0

