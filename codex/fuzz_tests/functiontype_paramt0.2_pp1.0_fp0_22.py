from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 可以设置函数的__name__属性
f = lambda x: x
f.__name__ = 'f'
f.__name__

# 可以设置函数的__doc__属性
f.__doc__ = 'f doc'
f.__doc__

# 可以设置函数的__dict__属性
f.__dict__ = {'a': 1}
f.__dict__

# 可以设置函数的__defaults__属性
f.__defaults__ = (1,)
f.__defaults__

# 可以设置函数的__closure__属性
f.__closure__ = (1,)
f.__closure__

# 可以设置
