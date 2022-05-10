import types
# Test types.FunctionType
function = types.FunctionType(codeobj, globals(), 'function')
print(function.__name__)
function()
# Test types.GeneratorType
generator = types.GeneratorType(codeobj, globals(), 'generator')
print(generator.__name__)
list(generator())
# Test types.CoroutineType
coroutine = types.CoroutineType(codeobj, globals(), 'coroutine')
print(coroutine.__name__)
list(coroutine())

# Test types.MethodType
class A: pass
A.method = types.MethodType(codeobj, A())
print(A.method.__name__)
A.method()

# Test types.BuiltinFunctionType
A.builtin_function = types.BuiltinFunctionType(len, globals())
print(A.builtin_function.__name__)
A.builtin_function([1, 2, 3])

# Test types.BuiltinMethodType
A.builtin_method = types.BuiltinMethodType(len, A())
print(A.builtin
