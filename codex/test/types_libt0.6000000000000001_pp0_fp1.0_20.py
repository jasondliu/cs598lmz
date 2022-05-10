import types
types.MethodType(func, obj)
obj.func()

def add_attr(obj, name, func):
    setattr(obj, name, types.MethodType(func, obj))

add_attr(obj, 'func', func)
obj.func()

# python的函数是对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

# 函数对象有一个__name__属性，可以拿到函数的名字
func.__name__

# 通过装饰器（decorator）可以给函数动态加上功能
# 这种在
