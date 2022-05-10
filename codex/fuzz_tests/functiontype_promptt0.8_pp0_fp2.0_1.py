import types
# Test types.FunctionType
assert issubclass(types.FunctionType, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, types.TypeType)
assert issubclass(types.BuiltinFunctionType, types.TracebackType)
try:
    import _tkinter
except ImportError:
    pass
else:
    assert not issubclass(_tkinter.Tcl_Obj, types.TracebackType)
# Test types.TracebackType
assert issubclass(types.TracebackType, types.FrameType)
assert not issubclass(types.FrameType, types.TracebackType)
# Test types.FrameType
assert not issubclass(types.FrameType, types.TracebackType)
assert issubclass(types.FrameType, types.CodeType)
# Test types.CodeType
assert issubclass(types.CodeType, types.TypeType)
assert issubclass(types.CodeType, types.ObjectType)
assert not issubclass(types.ObjectType, types.CodeType)
# Test types.ObjectType
assert not issub
