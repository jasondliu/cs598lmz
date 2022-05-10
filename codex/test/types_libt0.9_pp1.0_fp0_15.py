import types
types.MethodType(x._foo, y).__name__

# 'MethodType' object has no attribute '_foo'
# OK
types.MethodType(x._foo, y).__name__

# 'MethodType' object has no attribute '__name__'
# FAIL
name = types.MethodType(x._foo, y).__name__
__builtin__.types.MethodType(x._foo, y).__name__

# 'MethodType' object has no method '_foo'
# OK
name = x.__class__()._foo.__name__

# 'Function' object has no method '_func'
# FAIL
name = x.__class__()._func().__name__

# 'str' object has no method '_foo'
# OK
name = 'x'.__len__().__name__

# 'str' object has no method '_func'
# FAIL
name = 'x'._func(5).__name__

# 'types.IntType' object has no attribute '_foo'
# OK
types.IntType
