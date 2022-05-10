import types
# Test types.FunctionType
# Buggy types.FunctionType:
#fun = types.FunctionType(code, globals(), "fun")
# Correct types.FunctionType:
fun = types.FunctionType(code, globals())

print(fun())

# Buggy types.MethodType:
#meth = types.MethodType(fun, None, A)
# Correct types.MethodType:
#meth = types.MethodType(fun, None, A.__class__)
#meth = types.MethodType(fun, A())

# 
