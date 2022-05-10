import types
types.TypeType  # <class 'type'>

# type() 可以返回一个对象的类型
print(type(123))  # <class 'int'>
print(type('str'))  # <class 'str'>
print(type(None))  # <class 'NoneType'>

print(type(abs))  # <class 'builtin_function_or_method'>

# 判断一个对象是否是函数，可以使用types模块中定义的常量
def fn():
    pass

print(type(fn) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type((x for x in range(10))) == types.GeneratorType)  # True

# 使用isinstance()
#
