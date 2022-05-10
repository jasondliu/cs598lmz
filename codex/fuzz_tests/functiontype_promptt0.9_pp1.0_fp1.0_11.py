import types
# Test types.FunctionType
TestError( isinstance(types.FunctionType, types.BuiltinFunctionType),
             0 )

TestError( isinstance(types.FunctionType, types.TypeType),
             0 )

TestError( types.FunctionType.__name__,
             'function' )

TestError( len(types.FunctionType.__mro__),
             2 )

TestError( types.FunctionType.__mro__[0],
             types.FunctionType )

TestError( types.FunctionType.__mro__[1],
             types.TypeType )

TestError( types.FunctionType.__base__,
             types.TypeType )

def f():
    pass

TestError( isinstance(f, types.BuiltinFunctionType),
             0 )

TestError( isinstance(f, types.TypeType),
             0 )

TestError( types.FunctionType.__name__,
             'function' )

TestError( len(types.FunctionType.__mro__),
             2 )

TestError( types.FunctionType.__
