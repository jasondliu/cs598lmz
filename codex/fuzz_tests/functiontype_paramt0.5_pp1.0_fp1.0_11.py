from types import FunctionType
list(FunctionType(lambda x,y:x+y, globals(), 'add'))

# 判断对象是否是函数
def is_function(obj):
    return isinstance(obj, FunctionType)

# 判断对象是否是函数
def is_function2(obj):
    return hasattr(obj, '__call__')

# 判断对象是否是函数
def is_function3(obj):
    return hasattr(obj, '__code__')

# 判断对象是否是函数
def is_function4(obj):
    return hasattr(obj, '__closure__')

# 判断对象是否是函数
def is_function5(obj):
    return hasattr(obj, '__defaults__')

# 判断对象是否是函数
def is_function
