from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'foo', f.func_defaults, f.func_closure))

# 注意：
# 在Python 3.0中，创建一个新的函数对象，需要使用types.FunctionType()
# 在Python 2.6中，可以使用types.FunctionType()或者函数对象的__new__()方法
# 在Python 2.4和2.5中，只能使用函数对象的__new__()方法

# 如果你想构造一个匿名函数，可以使用lambda表达式
add = lambda x, y: x + y
add(2, 3)

# 函数对
