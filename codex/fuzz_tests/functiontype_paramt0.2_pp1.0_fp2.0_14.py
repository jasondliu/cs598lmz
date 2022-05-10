from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test __repr__
import types
def f(): pass
types.FunctionType(f.__code__, f.__globals__, 'foo', f.__defaults__, f.__closure__)

# Test __reduce__
import types
def f(): pass
types.FunctionType(f.__code__, f.__globals__, 'foo', f.__defaults__, f.__closure__).__reduce__()

# Test __reduce_ex__
import types
def f(): pass
types.FunctionType(f.__code__, f.__globals__, 'foo', f.__defaults__, f.__closure__).__reduce_ex__(2)

# Test __sizeof__
import types
def f(): pass
types.FunctionType(f.__code__, f.__globals__, 'foo', f.__defaults__, f.__closure__).__sizeof__()

# Test __subclasshook__
import types
def f
