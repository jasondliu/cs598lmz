import types
# Test types.FunctionType
try:
    f = types.FunctionType(lambda x: x)
    assert f(42) == 42
except:
    print("SKIP")
    raise SystemExit

# Test types.MethodType
class X:
    def __init__(self, x):
        self.x = x
assert types.MethodType(lambda self: self.x, X("hello"))().x == "hello"

# Test types.BuiltinMethodType
import sys
assert types.BuiltinMethodType(sys.exit) == sys.exit

# Test types.BuiltinFunctionType
assert types.BuiltinFunctionType(len) == len

# Test types.CodeType
try:
    assert types.CodeType(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")
except:
    print("SKIP")
    raise SystemExit

# Test types.FrameType
try:
    f = types.FrameType(None, None, None, 0)
    assert f.f_lineno == 0
except:
    print("SKIP")

