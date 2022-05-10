import types
# Test types.FunctionType
f = types.FunctionType(types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b''), {})
f()

# Test types.BuiltinFunctionType
f = types.BuiltinFunctionType(lambda: None)
f()

# Test types.MethodType
f = types.MethodType(lambda self: None, None)
f()

# Test types.MethodDescriptorType
f = types.MethodDescriptorType(lambda self: None)
f()

# Test types.UnboundMethodType
f = types.UnboundMethodType(lambda self: None, None, None)
f()

# Test types.ModuleType
f = types.ModuleType('name')
f

# Test types.TracebackType
f = types.TracebackType(None, None, None, None)
f

# Test types.FrameType
f = types.FrameType(None, None, None)
f

# Test types.GetSetDescriptorType
f = types.GetSetDescriptorType
