from types import FunctionType
list(FunctionType(lambda: 0, {}, "", (), ()))

import types
def f(): pass
list(types.FunctionType(f.__code__, {}, "", (), ()))

list(types.CodeType(0, {}, (), (), "", "", 0, "", (), (), ()))

class C:
    pass
list(types.FrameType(C(), C(), C(), C(), C()))

list(types.TracebackType(C(), C(), C(), C()))

list(types.GetSetDescriptorType(C(), C(), C(), C()))

list(types.MemberDescriptorType(C(), C(), C(), C()))

list(types.MappingProxyType({"a": 1}))

list(types.SimpleNamespace())

list(types.Namespace(x=1))

class C:
    def __new__(cls, x):
        return x

list(C("hi"))

class C:
    def __new__(cls, x):
        return x
    def __init__(
