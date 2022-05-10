import types
# Test types.FunctionType
if not isinstance(isinstance, types.FunctionType):
    raise RuntimeError("class types.FunctionType not defined")
# Test types.BuiltinFunctionType
if not isinstance(isinstance, types.BuiltinFunctionType):
    raise RuntimeError("class types.BuiltinFunctionType not defined")
# Test types.ClassType
if not isinstance(object, types.ClassType):
    raise RuntimeError("class types.ClassType not defined")
# Test types.TypeType
if not isinstance(type, types.TypeType):
    raise RuntimeError("class types.TypeType not defined")
# Test types.UnicodeType
if not isinstance(u'', types.UnicodeType):
    raise RuntimeError("class types.UnicodeType not defined")
# Test types.StringType
if not isinstance('', types.StringType):
    raise RuntimeError("class types.StringType not defined")
# Test types.NoneType
if not isinstance(None, types.NoneType):
    raise RuntimeError("class types.NoneType not defined")
# Test types.ComplexType
if
