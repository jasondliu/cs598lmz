import types
# Test types.FunctionType
result = types.FunctionType(None, globals())
result = types.FunctionType(None, None)
result = types.FunctionType(
    lambda *args, **kwargs: None, globals(), 'myname')
result = types.FunctionType(
    lambda *args, **kwargs: None, None, 'myname')
 
# Test types.CodeType
result = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0,
    b'')
result = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0,
    b'', (), (), ())
 
# Test types.MethodType
result = types.MethodType(lambda self: None, None)
result = types.MethodType(lambda self: None, None, types.StringType)
result = types.MethodType(lambda self: None, None, types.StringType,
    types.StringType)
result = types.MethodType(lambda self: None, None, types.StringType,
    types.StringType, True
