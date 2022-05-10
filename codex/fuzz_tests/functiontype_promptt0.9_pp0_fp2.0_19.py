import types
# Test types.FunctionType is importable
# Test types.LambdaType is importable
# Test types.CodeType is importable
import types

def f(x):
    return x + 1

t = types.FunctionType(f.__code__, {}, "f", (1,), (1,))
t == f
t.__code__

def g():
    return 2

t = types.FunctionType(g.__code__, {}, "g", (), ())
t == g
t.__code__

t = types.LambdaType(lambda: 1, {})
t
list(t.__code__.co_freevars), t.__closure__

# Test types.FrameType is importable
# Test types.MethodType is importable
import types

def f(x): return x**2
method = types.MethodType(f, 42)
method
method()
method('spam')

import types
types.FrameType

# Test types.GeneratorType is importable
# Test types.TracebackType is importable
import types
types
