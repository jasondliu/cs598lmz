import types
# Test types.FunctionType with a UserFunction.
from _pydecimal import Decimal
def f(): pass
assert type(f) is types.FunctionType
f1 = f
assert type(f) is type(f1)
assert type(f) is types.FunctionType

from inspect import currentframe
def GetFrame():
    cf = currentframe(1)
    return cf

assert type(GetFrame) is types.FunctionType

cf = GetFrame()
assert type(GetFrame) is types.FunctionType

def GetFrameAndDec():
    cf = currentframe(1)
    d = Decimal('3')
    return cf, d

cfd = GetFrameAndDec()
assert type(GetFrameAndDec) is types.FunctionType

class f():
    def __init__(self):
        pass

assert type(f) is type

class f():
    def __init__(self):
        pass

f1 = f
assert type(f) is type
assert type(f) is type(f1)

assert type(f()) is f

class f():
