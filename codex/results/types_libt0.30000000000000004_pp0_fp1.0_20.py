import types
types.MethodType(lambda self: 42, None)

# TypeError: can't set attributes of built-in/extension type 'function'
# types.FunctionType(lambda: 42, {})

# TypeError: can't set attributes of built-in/extension type 'method'
# types.MethodType(lambda: 42, None)

# TypeError: can't set attributes of built-in/extension type 'builtin_function_or_method'
# types.BuiltinFunctionType(lambda: 42)

# TypeError: can't set attributes of built-in/extension type 'builtin_function_or_method'
# types.BuiltinMethodType(lambda: 42)

# TypeError: can't set attributes of built-in/extension type 'method_descriptor'
# types.MethodDescriptorType(lambda: 42)

# TypeError: can't set attributes of built-in/extension type 'wrapper_descriptor'
# types.WrapperDescriptorType(lambda: 42)

# TypeError: can't set attributes of built-in/ext
