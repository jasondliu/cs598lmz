import ctypes
# Test ctypes.CFUNCTYPE
# https://docs.python.org/3/library/ctypes.html

# test function
def add_simple(a, b):
    return a + b

# test function
def add_complex(a, b):
    return a.real + a.imag + b.real + b.imag

# test function
def add_array(a, b, count):
    for i in range(0, count):
        a[i] += b[i]
    return a

def test_c_function(c_function):
    assert c_function(1, 2) == 3
    assert c_function(1.2, 3.4) == 4.6
    assert c_function(1.2 + 2.3j, 3.4 + 4.5j) == 9.4 + 6.8j
    assert c_function([1, 2, 3, 4], [5, 6, 7, 8], 4) == [6, 8, 10, 12]

# create C type
c_int = ctypes.c_int
c_float = ctypes.
