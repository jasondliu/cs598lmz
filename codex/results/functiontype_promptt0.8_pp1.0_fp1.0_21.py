import types
# Test types.FunctionType
# src/__init__.py +2
def _function_type_check(obj):
    return isinstance(obj, types.FunctionType)

# Test types.CodeType
# src/__init__.py +6
def _code_type_check(obj):
    return isinstance(obj, types.CodeType)

# Test types.UnboundMethodType
# src/__init__.py +10
def _unbound_method_type_check(obj):
    return isinstance(obj, types.UnboundMethodType)

# Test types.MethodType
# src/__init__.py +14
def _method_type_check(obj):
    return isinstance(obj, types.MethodType)

# Test types.BuiltinFunctionType
# src/__init__.py +18
def _builtin_function_type_check(obj):
    return isinstance(obj, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
# src/__init__.py +22
def _builtin_method_type_check(obj
