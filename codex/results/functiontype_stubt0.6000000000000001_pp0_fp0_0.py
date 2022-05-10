from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(abs))
print(type(a) == types.GeneratorType)
print(type(lambda x: x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.FunctionType)
print(isinstance(a, types.GeneratorType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.FunctionType))

import datetime
print(type(datetime.datetime.now()) == datetime.datetime)
print(isinstance(datetime.datetime.now(), datetime.datetime))
