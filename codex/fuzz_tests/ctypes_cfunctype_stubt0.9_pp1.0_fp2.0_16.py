import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun()() == 42
# Test return of simple structures
@FUNTYPE
def fun():
    return (1, 2)
assert fun()() == (1, 2)

# Test return of tuples with inner structures
@FUNTYPE
def fun():
    return ((1, 2), (3, (4, 5)))
assert fun()() == ((1, 2), (3, (4, 5)))

# Test return of tuples with inner structures
@FUNTYPE
def fun():
    return ((1, 2), (3, (4, (5, 6))))
assert fun()() == ((1, 2), (3, (4, (5, 6))))

# Test return of lists with inner structures
@FUNTYPE
def fun():
    return [[1, 2], [3, (4, 5)]]
assert fun()() == [[1, 2], [3, (4, 5)]]

# Test return of lists with inner structures
@FUNTYPE
def fun():
    return [[1, 2], [3, (4, (5, 6))]]
assert fun()
