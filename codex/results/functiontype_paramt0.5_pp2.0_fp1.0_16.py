from types import FunctionType
list(FunctionType(FunctionType.__code__, {}, None))

# test __repr__
def f():
    pass
f.__code__ = f.__code__
f.__code__()

# test __sizeof__
import sys
def f():
    pass

sys.getsizeof(f.__code__)

# test __reduce__
def f():
    pass
f.__code__ = f.__code__
f.__code__()

# test __reduce_ex__
def f():
    pass
f.__code__ = f.__code__
f.__code__()
