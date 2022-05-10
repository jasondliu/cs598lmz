import types
# Test types.FunctionType
def func():
    pass
# FunctionType
print(type(func))
# <class 'function'>
print(type(abs))
# <class 'builtin_function_or_method'>
print(type(lambda x: x))
# <class 'function'>
print(type((x for x in range(10))))
# <class 'generator'>
print(type(x for x in range(10)))
# <class 'generator'>
# Test types.BuiltinFunctionType
print(type(abs))
# <class 'builtin_function_or_method'>
print(type(int))
# <class 'type'>
# Test types.LambdaType
print(type(lambda x: x))
# <class 'function'>
# Test types.GeneratorType
print(type((x for x in range(10))))
# <class 'generator'>
print(type(x for x in range(10)))
# <class 'generator'>
# Test types.TracebackType
try:
    10 / 0
except ZeroDivisionError as e:
    print(
